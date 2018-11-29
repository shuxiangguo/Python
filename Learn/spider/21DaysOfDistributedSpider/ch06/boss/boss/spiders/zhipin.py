# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem

class ZhipinSpider(CrawlSpider):
	name = 'zhipin'
	allowed_domains = ['zhipin.com']
	start_urls = ['http://zhipin.com/']

	rules = (
		# 匹配职位列表页规则
		Rule(LinkExtractor(allow=r'.+\?query=python&page=\d'), follow=True),

		# 匹配下载详情页规则
		Rule(LinkExtractor(allow=r'.+job_detail/.+.htm'), callback='parse_job', follow=False),
	)

	def parse_job(self, response):
		title = response.xpath("//div[@class='name']/h1/text()").get()
		salary = response.xpath()

		item = BossItem(titl=title, salary=salary)
		yield item