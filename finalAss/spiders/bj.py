import scrapy
from finalAss.items import BJItem


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


class BjSpider(scrapy.Spider):
    name = "bj"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ["https://bj.lianjia.com/zufang/"]
    custom_settings = {
        "ITEM_PIPELINES": {
            "finalAss.pipelines.MyPipeline": 400,
        },
        "FIELDS_TO_EXPORT": [
            "名称",
        ],
    }

    def parse(self, response):
        for each in response.css(".content__list--item"):
            isOK = True
            item = BJItem()
            info = each.css("a.content__list--item--aside[title]::attr(title)").extract_first()
            info_list = info.split(" ")
            item["名称"] = info_list[0][3:]

            typeList = [s for s in info_list if "室" in s or "房间" in s]
            item["房型"] = typeList[0] if len(typeList) > 0 else ""

            orientationList = [s for s in info_list if
                               len(s) in range(1, 4) and ("东" in s or "南" in s or "西" in s or "北" in s)]
            item["朝向"] = orientationList[0] if len(orientationList) > 0 else ""

            info = each.css("p.content__list--item--des a::text").getall()
            if len(info) > 2:
                item["区域"] = info[0]
                item["板块"] = info[1]
            else:
                item["区域"] = ""
                item["板块"] = ""

            info = each.css("p.content__list--item--des ::text").getall()
            areaList = [s for s in info if "㎡" in s]
            item["面积"] = areaList[0].strip() if len(areaList) > 0 else ""
            pass
            # item = NewHouseItem()
            # item["楼盘名称"] = each.css(".resblock-name .name::text").get().strip()
            # item["类型"] = each.css(".resblock-type::text").get().strip()
            # item["地理位置"] = each.css(".resblock-location a::text").get().strip()
            # item["房型"] = each.css(".resblock-room span::text").getall()

            # # 消除前三个多余字符
            # area = each.css(".resblock-area span::text").get()
            # item["面积"] = "" if area is None else area

            # item["均价"] = each.css(".main-price span::text").get()
            # total = each.css(".second::text").get()
            # item["总价"] = "" if total is None else total
            if isOK:
                yield item
        pass
