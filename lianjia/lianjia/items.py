# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseItem(scrapy.Item):
    楼盘名称 = scrapy.Field()
    类型 = scrapy.Field()
    地理位置 = scrapy.Field()
    房型 = scrapy.Field()
    面积 = scrapy.Field()
    均价 = scrapy.Field()
    总价 = scrapy.Field()
    pass


class ESFHouseItem(scrapy.Item):
    楼盘名称 = scrapy.Field()
    地理位置 = scrapy.Field()
    房型 = scrapy.Field()
    面积 = scrapy.Field()
    均价 = scrapy.Field()
    总价 = scrapy.Field()
    pass
