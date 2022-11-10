# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.http import HtmlResponse
from logging import getLogger
import time

class WeiboCrawlerSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class WeiboCrawlerDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = 100
        self.browser = webdriver.Chrome(executable_path='path to your chromedriver')
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)
        self.stage = 0

    def __del__(self):
        self.browser.close()

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        try:
            self.browser.get(request.url)
            if request.meta['login'] is False:
                time.sleep(8)
                self.browser.find_element_by_css_selector("#loginname").send_keys(
                    "your login name")
                self.browser.find_element_by_css_selector(".info_list.password input[node-type='password']").send_keys(
                    "your password")
                self.browser.find_element_by_css_selector('#login_form_savestate').click()
                self.browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").click()
                input()
                self.browser.get(request.url)

            js = "return action=document.body.scrollHeight"
            height = self.browser.execute_script(js)
            count = 0

            while True:
                self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                new_height = self.browser.execute_script(js)
                time.sleep(1)
                if new_height <= height:
                    try:
                        button_more = self.browser.find_element_by_css_selector(
                            '.more_txt.W_f14')
                        count = 0
                        button_more.click()
                    except:
                        try:
                            loading_sign = self.browser.find_element_by_css_selector('.W_loading')
                            if count < 10:
                                print("等待中...")
                                count += 1
                                time.sleep(2)
                                continue
                            else:
                                choice = input()
                                if choice == 'y':
                                    print("已至底部")
                                    input()
                                    break
                                else:
                                    count = 0
                                    time.sleep(2)
                                    continue
                        except:
                            print("已至底部")
                            input()
                            break
                else:
                    print("here??")
                    height = self.browser.execute_script(js)

            return HtmlResponse(url=self.browser.current_url, body=self.browser.page_source, encoding='utf-8')
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class FakeWeiboDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = 100
        self.browser = webdriver.Chrome(executable_path='path to your chromedriver')
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)
        self.stage = 0

    def __del__(self):
        self.browser.close()

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        try:
            self.browser.get(request.url)
            if request.meta['login'] is False:
                time.sleep(8)
                self.browser.find_element_by_css_selector("#loginname").send_keys(
                    "your login name")
                self.browser.find_element_by_css_selector(".info_list.password input[node-type='password']").send_keys(
                    "your password")
                self.browser.find_element_by_css_selector('#login_form_savestate').click()
                self.browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").click()
                input()
                self.browser.get(request.url)

            return HtmlResponse(url=self.browser.current_url, body=self.browser.page_source, encoding='utf-8')



        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
