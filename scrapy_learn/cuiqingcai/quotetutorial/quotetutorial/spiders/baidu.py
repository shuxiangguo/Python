# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def make_requests_from_url(self, url):
        return scrapy.Request(url=url, callback=self.parse_index)

    def parse_index(self, response):
        self.logger.info(response.status)

    def parse(self, response):
        pass
