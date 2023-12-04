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
        self.file = open(spider.name + ".csv", "w", encoding="utf-8-sig")
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        self.writer.writerow(
            [
                item["名称"],
            ]
        )
        return item

    def close_spider(self, spider):
        self.file.close()
