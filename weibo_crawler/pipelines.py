# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

class WeiboCrawlerPipeline(object):
    def __init__(self):
        self.filename = "normal_weibo.json"
        self.file = open(self.filename, "w", encoding="utf-8")
    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False, indent=4) + "\n")
        return item
    def spider_closed(self, spider):
        self.file.close()

class FakeWeiboPipeline(object):
    def __init__(self):
        self.filename = "rumor_weibo.json"
        self.file = open(self.filename, "w", encoding="utf-8")
    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False, indent=4) + "\n")
        return item
    def spider_closed(self, spider):
        self.file.close()
