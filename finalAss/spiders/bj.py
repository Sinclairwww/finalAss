import scrapy
from finalAss.items import BJItem


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


class BjSpider(scrapy.Spider):
    name = "bj"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ["https://bj.lianjia.com/zufang/#contentList"]
    # prefix = "https://bj.lianjia.com/zufang/pg"
    # index = 2

    custom_settings = {
        "ITEM_PIPELINES": {
            "finalAss.pipelines.MyPipeline": 400,
            "finalAss.pipelines.bjPipeline": 300,
        },
    }

    def parse_item(self, selector):
        isOK = True
        item = BJItem()
        info = selector.css("a.content__list--item--aside[title]::attr(title)").extract_first()
        info_list = info.split(" ")
        item["名称"] = info_list[0][3:]

        typeList = [s for s in info_list if "室" in s or "房间" in s]
        item["房型"] = typeList[0] if len(typeList) > 0 else ""

        orientationList = [s for s in info_list if
                           len(s) in range(1, 4) and ("东" in s or "南" in s or "西" in s or "北" in s)]
        item["朝向"] = orientationList[0] if len(orientationList) > 0 else ""

        info = selector.css("p.content__list--item--des a::text").getall()
        if len(info) > 2:
            item["区域"] = info[0]
            item["板块"] = info[1]
        else:
            item["区域"] = ""
            item["板块"] = ""

        info = selector.css("p.content__list--item--des ::text").getall()
        areaList = [s for s in info if "㎡" in s]
        item["面积"] = areaList[0].strip() if len(areaList) > 0 else ""

        item["价格"] = selector.css('span.content__list--item-price em::text').get()
        item["单位面积价格"] = ""
        yield item

    def parse(self, response):
        for each in response.css(".content__list--item"):
            item = self.parse_item(each)
            yield item

        next_page = response.css("#content > div.content__article > div.content__pg > a.next").extract_first()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            return None
