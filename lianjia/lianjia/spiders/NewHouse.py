import scrapy
from lianjia.items import NewHouseItem


class NewHouseSpider(scrapy.Spider):
    name = "NewHouse"
    allowed_domains = ["bj.fang.lianjia.com"]
    custom_settings = {
        "ITEM_PIPELINES": {
            "lianjia.pipelines.MyPipeline": 400,
            "lianjia.pipelines.NewHousePreprocessPipeline": 300,
        }
    }
    rootUrl = "https://bj.fang.lianjia.com/loupan/pg"
    index = 4
    start_urls = ["https://bj.fang.lianjia.com/loupan/pg3/"]

    def parse(self, response):
        for each in response.css(".resblock-desc-wrapper"):
            item = NewHouseItem()
            item["楼盘名称"] = each.css(".resblock-name .name::text").get().strip()
            item["类型"] = each.css(".resblock-type::text").get().strip()
            item["地理位置"] = each.css(".resblock-location a::text").get().strip()
            item["房型"] = each.css(".resblock-room span::text").getall()

            # 消除前三个多余字符
            area = each.css(".resblock-area span::text").get()
            item["面积"] = "" if area is None else area

            item["均价"] = each.css(".main-price span::text").get()
            total = each.css(".second::text").get()
            item["总价"] = "" if total is None else total

            yield item

        if self.index <= 7:
            url = self.rootUrl + str(self.index) + "/"
            self.index += 1
            yield scrapy.Request(url, callback=self.parse)
