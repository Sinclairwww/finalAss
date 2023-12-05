# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import re
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import csv


class MyPipeline(object):
    def __init__(self):
        self.writer = None
        self.file = None

    def open_spider(self, spider):
        self.file = open(spider.name + ".csv", "w", newline='', encoding="utf-8-sig")
        self.writer = csv.writer(self.file)
        self.writer.writerow(
            [
                "名称",
                "区域",
                "板块",
                "房型",
                "朝向",
                "面积",
            ]
        )

    def process_item(self, item, spider):
        self.writer.writerow(
            [
                item["名称"],
                item["区域"],
                item["板块"],
                item["房型"],
                item["朝向"],
                item["面积"],
            ]
        )
        return item

    def close_spider(self, spider):
        self.file.close()


# class bjPipeline(object):
#     def __init__(self):
#         self.writer = None
#         self.file = None

#     def open_spider(self, spider):
#         self.file = open(spider.name + ".csv", "w", encoding="utf-8-sig")
#         self.writer = csv.writer(self.file)

#     def process_item(self, item, spider):
#         self.writer.writerow(
#             [
#                 item["楼盘名称"],
#                 item["类型"],
#                 item["地理位置"],
#                 item["房型"],
#                 item["面积"],
#                 item["均价"],
#                 item["总价"],
#             ]
#         )
#         return item

#     def close_spider(self, spider):
#         self.file.close()
