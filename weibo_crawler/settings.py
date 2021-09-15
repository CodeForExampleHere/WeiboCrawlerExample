# -*- coding: utf-8 -*-

# Scrapy settings for weibo_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibo_crawler'

SPIDER_MODULES = ['weibo_crawler.spiders']
NEWSPIDER_MODULE = 'weibo_crawler.spiders'

# LOG_LEVEL = 'INFO'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibo_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
   'Cookie':'login_sid_t=17ef9874b4f651eefef080842f6f3e93; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=7761125586879.216.1581909478783; SINAGLOBAL=7761125586879.216.1581909478783; ULV=1581909478799:1:1:1:7761125586879.216.1581909478783:; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhPdj8IaVDw1s9JEgm.EzEL5JpX5K2hUgL.Fo2RSK.pehzceKz2dJLoIpxhB-4i-XyWCXHH-Lilg-8eC281x5tt; SSOLoginState=1581909545; ALF=1613445556; SCF=AsCgLr-M5sL__LLmxsqU2O_6oYxV4CFAttlk8vqB9sl82lericUHgM-bPW68zTL8T_Hkca0qiKWl8cWxro-kXBc.; SUB=_2A25zTnZlDeRhGedG7lsQ8CzKyj6IHXVQOuCtrDV8PUNbmtAfLVmgkW9NUVW4CjRdUdC3uD7NBZiB4s9797K7EHwA; SUHB=0h1YmvzHq2Ras4; un=1156618076@qq.com; wvr=6; webim_unReadCount=%7B%22time%22%3A1581909566684%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A1%2C%22msgbox%22%3A0%7D'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'weibo_crawler.middlewares.WeiboCrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'weibo_crawler.middlewares.WeiboCrawlerDownloaderMiddleware': 543
   # 'weibo_crawler.middlewares.FakeWeiboDownloaderMiddleware': 543

}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'weibo_crawler.pipelines.WeiboCrawlerPipeline': 300
   # 'weibo_crawler.pipelines.FakeWeiboPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
