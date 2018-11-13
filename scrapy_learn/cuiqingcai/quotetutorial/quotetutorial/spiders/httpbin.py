# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/post']

    def start_requests(self):
        yield scrapy.Request(url="http://httpbin.org/post", method="POST", callback=self.parse_post)

    def parse_post(self, response):
        print("hello ", response.status)


    def parse(self, response):
        pass
