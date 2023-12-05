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

from unicodedata import decimal


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
                "面积(平米)",
                "价格(元/月)",
                "单位面积价格(元/平米/月)"
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
                item["价格"],
                item["单位面积价格"],
            ]
        )
        return item

    def close_spider(self, spider):
        self.file.close()


class bjPipeline(object):
    def process_item(self, item, spider):
        if "面积" in item:
            if item["面积"] != "":
                numbers = re.findall(r"\d+", item["面积"])
                numbers = [int(x) for x in numbers]
                item["面积"] = sum(numbers) / len(numbers)

        if "价格" in item:
            if item["价格"] != "":
                numbers = re.findall(r"\d+", item["价格"])
                numbers = [int(x) for x in numbers]
                item["价格"] = int(sum(numbers) / len(numbers))

        if "单位面积价格" in item:
            if item["面积"] != "" and item["价格"] != "":
                item["单位面积价格"] = int(item["价格"] / item["面积"])

        return item
