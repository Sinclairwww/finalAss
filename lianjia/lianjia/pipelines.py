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
        self.writer.writerow([
            item['楼盘名称'],
            item['类型'],
            item['地理位置'],
            item['房型'],
            item['面积'],
            item['均价'],
            item['总价'],
        ])
        return item

    def close_spider(self, spider):
        self.file.close()



class NewHousePreprocessPipeline(object):
    def process_item(self, item, spider):
        # 去除字段两端的空白字符
        if '楼盘名称' in item:
            item['楼盘名称'] = item['楼盘名称'].strip()

        if '面积' in item:
            if item['面积'] != "":
                numbers = re.findall(r'\d+', item['面积'])
                numbers = [int(x) for x in numbers]
                item['面积'] = numbers[0]

        if '均价' in item:
            try:
                item['均价'] = int(item['均价'])
            except ValueError:
                raise DropItem(f"无法转换数量: {item['均价']}")

        if '总价' in item:
            item['总价'] = item['总价'][2:-5]
            numbers = re.findall(r'\d+', item['总价'])
            numbers = [int(x) for x in numbers]
            item['总价'] = numbers[0]

        if '房型' in item:
            if len(item['房型']) >= 1:
                item['房型'] = item['房型'][0]
        return item
