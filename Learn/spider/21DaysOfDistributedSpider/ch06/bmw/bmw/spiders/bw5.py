# -*- coding: utf-8 -*-
import scrapy
from bmw.items import BmwItem

class Bw5Spider(scrapy.Spider):
	name = 'bw5'
	allowed_domains = ['car.autohome.com.cn']
	start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

	def parse(self, response):
		uiboxs = response.xpath('//div[@class="uibox"]')[1:]
		for box in uiboxs:
			category = box.xpath('.//div[@class="uibox-title"]/a/text()').get()
			urls = box.xpath('.//ul/li/a//img/@src').getall()
			# for url in urls:
			# 	url = response.urljoin(url)
			# 	print(url)
			urls = list(map(lambda url : response.urljoin(url), urls))

			item = BmwItem(category=category, urls=urls)
			yield item

