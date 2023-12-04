import scrapy
from finalAss.items import BJItem


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
            item = BJItem()
            item["名称"] = each.css("a.twoline::text").get().strip()
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

            yield item
        pass
