# -*- coding: utf-8 -*-
import scrapy
from weibo_crawler import utils
from weibo_crawler.items import WeiboItem


class UnrealSpider(scrapy.Spider):
    name = 'unreal'
    allowed_domains = ['weibo.com']
    start_urls = ['https://service.account.weibo.com/index?type=5&status=0&page=302']
    cookies = "SINAGLOBAL=6829046407402.302.1519650564247; _s_tentry=www.baidu.com; Apache=9464261931068.988.1578307139731; ULV=1578307139746:26:1:1:9464261931068.988.1578307139731:1577676276865; UM_distinctid=16f7a82aef3cd-00ca96c5a2e13a-1d376b5d-1fa400-16f7a82aef41c6; login_sid_t=704d202743692a6a5463bf28f9f024b2; cross_origin_proto=SSL; UOR=,,login.sina.com.cn; appkey=; WBtopGlobal_register_version=307744aa77dd5677; PHPSESSID=6tnb3b4d5gud114oon8hkakj26; un=1156618076@qq.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhPdj8IaVDw1s9JEgm.EzEL5JpX5K2hUgL.Fo2RSK.pehzceKz2dJLoIpxhB-4i-XyWCXHH-Lilg-8eC281x5tt; SCF=ApVq1k2A-mGoH-u-0BETtIem43c8AAmwe4QwWh0paHNt9seW-PITytDWU86qbO-tzTex3HvK3ytUfwv8fyqm4Ao.; SUB=_2A25zVwGGDeRhGedG7lsQ8CzKyj6IHXVQJXROrDV8PUNbmtAfLVH-kW9NUVW4CkDtZPaQnVB3HQbwOFtnmyOCfGRg; SUHB=0OM1_pM1-HXSDO; webim_unReadCount=%7B%22time%22%3A1582526940458%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; wvr=6"

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
