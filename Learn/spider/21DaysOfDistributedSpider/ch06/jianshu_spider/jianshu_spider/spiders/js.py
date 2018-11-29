# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from jianshu_spider.items import JianshuSpiderItem
class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath("//a[@class='avatar']/img/@src").get()
        author = response.xpath("//span[@class='name']/a/text()").get()
        pub_time = response.xpath("//div[@class='meta']/span[@class='publish-time']/text()").get().replace("*", '')

        # https://www.jianshu.com/p/a38149439483
        # https://www.jianshu.com/p/b485271a9945?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
        url = response.url #url存在上面注释中的俩种情况

        # 如果是第一种，分割后url1是 [https://www.jianshu.com/p/a38149439483]
        # 如果是第二种，分割收url1是 [https://www.jianshu.com/p/a38149439483, utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation]
        url1 = url.split('?')
        url2 = url1[0]

        article_id = url2.split('/')[-1] # 拿到id
        content = response.xpath("//div[@class='show-content-free']").get()

        item = JianshuSpiderItem(
            title=title,
            author=author,
            content=content,
            pub_time=pub_time,
            avatar=avatar,
            original_url = url,
            article_id=article_id
        )
        yield item