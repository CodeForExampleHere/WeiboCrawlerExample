# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ouid = scrapy.Field()
    mid = scrapy.Field()
    url = scrapy.Field()
    domain = scrapy.Field()
    # time = scrapy.Field()
    # comment_count = scrapy.Field()
    pass

class WeiboItem(scrapy.Item):
    uid = scrapy.Field()
    mid = scrapy.Field()
    url = scrapy.Field()
    pass