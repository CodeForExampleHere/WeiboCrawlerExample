# -*- coding: utf-8 -*-
import scrapy
import utils
from items import WeiboItem

class UnrealSpider(scrapy.Spider):
    name = 'unreal'
    allowed_domains = ['weibo.com']
    start_urls = ['https://service.account.weibo.com/index?type=5&status=0&page=302']
    cookies = "your_cookies"

    def start_requests(self):
        headers = {'cookie':self.cookies}
        yield scrapy.Request(url = self.start_urls[0], headers=headers, meta={"login": False})

    def parse(self, response):

        root = "https://service.account.weibo.com/index?type=5&status=0&page="

        if 'page_num' in response.meta:
            pass
        else:
            response.meta['page_num'] = 302

        list = response.css(".m_table_tit a")
        for title in list:
            content = title.css('::attr(href)').extract_first()
            detail_url = "https://service.account.weibo.com" + content
            yield scrapy.Request(url=detail_url, callback = self.getId, meta={'login': True})

        if response.meta['page_num'] < 500:
            response.meta['page_num'] += 1
            next_url = root + str(response.meta['page_num'])
            yield scrapy.Request(url = next_url, callback=self.parse, meta={'page_num': response.meta['page_num'], 'login': True})



    def getId(self, response):
        publisher = response.css('.publisher a')
        url = publisher.css('::attr(href)').extract_first()
        item = WeiboItem()
        info = url.split('/')
        item['uid'] = info[-2]
        item['mid'] = utils.url_to_mid(info[-1])
        item['url'] = url
        yield item
