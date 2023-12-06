import scrapy
from finalAss.items import BJItem


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


class BjSpider(scrapy.Spider):
    name = "bj"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = [
        "https://bj.lianjia.com/zufang/dongcheng/",
        "https://bj.lianjia.com/zufang/xicheng/",
        "https://bj.lianjia.com/zufang/chaoyang/",
        "https://bj.lianjia.com/zufang/haidian/",
        "https://bj.lianjia.com/zufang/fengtai/",
        "https://bj.lianjia.com/zufang/shijingshan/",
        "https://bj.lianjia.com/zufang/tongzhou/",
        "https://bj.lianjia.com/zufang/changping/",
        "https://bj.lianjia.com/zufang/daxing/",
        "https://bj.lianjia.com/zufang/yizhuangkaifaqu/",
        "https://bj.lianjia.com/zufang/shunyi/",
        "https://bj.lianjia.com/zufang/fangshan/",
        "https://bj.lianjia.com/zufang/mentougou/",
        "https://bj.lianjia.com/zufang/pinggu/",
        "https://bj.lianjia.com/zufang/huairou/",
        "https://bj.lianjia.com/zufang/miyun/",
        "https://bj.lianjia.com/zufang/yanqing/",
    ]

    index = {
        "dongcheng": 2,
        "xicheng": 2,
        "chaoyang": 2,
        "haidian": 2,
        "fengtai": 2,
        "shijingshan": 2,
        "tongzhou": 2,
        "changping": 2,
        "daxing": 2,
        "yizhuangkaifaqu": 2,
        "shunyi": 2,
        "fangshan": 2,
        "mentougou": 2,
        "pinggu": 2,
        "huairou": 2,
        "miyun": 2,
        "yanqing": 2,
    }

    prefix = "https://bj.lianjia.com/zufang/"

    custom_settings = {
        "ITEM_PIPELINES": {
            "finalAss.pipelines.MyPipeline": 400,
            "finalAss.pipelines.bjPipeline": 300,
        },
    }

    def parse_item(self, selector):
        item = BJItem()
        info = selector.css(
            "a.content__list--item--aside[title]::attr(title)"
        ).extract_first()
        info_list = info.split(" ")
        item["名称"] = info_list[0][3:]

        typeList = [s for s in info_list if "室" in s or "房间" in s]
        item["房型"] = typeList[0] if len(typeList) > 0 else ""

        orientationList = [
            s
            for s in info_list
            if len(s) in range(1, 4) and ("东" in s or "南" in s or "西" in s or "北" in s)
        ]
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

        item["价格"] = selector.css("span.content__list--item-price em::text").get()
        item["单位面积价格"] = ""
        return item

    def parse(self, response):
        for each in response.css(".content__list--item"):
            item = self.parse_item(each)
            yield item

        location = response.url.split("/")[4]
        idx = self.index[location]
        if idx <= 100:
            next_page = self.prefix + location + "/pg" + str(idx) + "/" + "#contentList"
            self.index[location] += 1
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            return None
