# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BasicItem(scrapy.Item):
    # define the fields for your item here like:
    名称 = scrapy.Field()
    房型 = scrapy.Field()
    朝向 = scrapy.Field()
    区域 = scrapy.Field()
    板块 = scrapy.Field()
    面积 = scrapy.Field()
    价格 = scrapy.Field()
    单位面积价格 = scrapy.Field()

    pass
