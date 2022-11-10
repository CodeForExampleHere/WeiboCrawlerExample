# -*- coding: utf-8 -*-
import scrapy
from items import WeiboCrawlerItem


class TimelineSpider(scrapy.Spider):
    name = 'timeline'
    allowed_domains = ['weibo.com']
    index = 0
    start_urls = ['https://d.weibo.com/102803_ctg1_4188_-_ctg1_4188?from=faxian_hot&mod=fenlei#',
                  'https://d.weibo.com/102803_ctg1_6288_-_ctg1_6288?from=faxian_hot&mod=fenlei#',
                  'https://d.weibo.com/102803_ctg1_2088_-_ctg1_2088?from=faxian_hot&mod=fenlei#',
                  'https://d.weibo.com/102803_ctg1_5988_-_ctg1_5988?from=faxian_hot&mod=fenlei#',
                  'https://d.weibo.com/102803_ctg1_6388_-_ctg1_6388?from=faxian_hot&mod=fenlei#',
                  'https://d.weibo.com/102803_ctg1_4688_-_ctg1_4688?from=faxian_hot&mod=fenlei#',
                  'https://d.weibo.com/102803_ctg1_1388_-_ctg1_1388?from=faxian_hot&mod=fenlei#',
                  'https://d.weibo.com/102803_ctg1_2188_-_ctg1_2188?from=faxian_hot&mod=fenlei#',
                  'https://d.weibo.com/102803_ctg1_2588_-_ctg1_2588?from=faxian_hot&mod=fenlei#'
                  ]

    domains = ['社会', '国际', '科技', '科普', '财经',
                '综艺', '体育', '健康', '旅游' ]

    def start_requests(self):
        for url in self.start_urls:
            if self.index == 0:
                yield scrapy.Request(url = url, callback=self.parse, meta={"login": False, "index": self.index})
            else:
                yield scrapy.Request(url = url, callback=self.parse, meta={"login": True, "index": self.index})
            self.index += 1


    def parse(self, response):

        list = response.css('div[action-type="feed_list_item"]')
        print("total: " + str(len(list)))
        input()

        for wb in list:
            item = WeiboCrawlerItem()
            item['ouid'] = wb.css('::attr(tbinfo)').extract_first()[5:]
            item['mid'] = wb.css('::attr(mid)').extract_first()
            item['url'] = wb.css('a[node-type="feed_list_item_date"]::attr(href)').extract_first()
            item['domain'] = self.domains[response.meta["index"]]
            yield item
