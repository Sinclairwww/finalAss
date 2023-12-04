import scrapy
from lianjia.items import ESFHouseItem


class ESFHouseSpider(scrapy.Spider):
    name = "ESFHouse"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ["https://bj.lianjia.com/ershoufang/pg3/"]
    rootUrl = "https://bj.lianjia.com/ershoufang/pg"
    index = 4
    custom_settings = {
        'ITEM_PIPELINES': {
            'lianjia.pipelines.MyPipeline': 400,
            'lianjia.pipelines.ESFPreprocessPipeline': 300
        }
    }

    def parse(self, response):
        for each in response.css(".info"):
            item = ESFHouseItem()
            info = each.css(".positionInfo a::text").getall()
            item["楼盘名称"] = info[0]
            item["地理位置"] = info[1]

            item["房型"] = each.css(".houseInfo::text").get()
            item["均价"] = each.css(".unitPrice span::text").get()
            item["总价"] = each.css(".totalPrice span::text").get()
            yield item

            if self.index <= 7:
                url = self.rootUrl + str(self.index) + "/"
                self.index += 1
                yield scrapy.Request(url, callback=self.parse)
