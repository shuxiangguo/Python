# -*- coding: utf-8 -*-
import scrapy
import re


class SfwSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['http://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]") #没有class属性的td标签
            province_td = tds[0]
            province_text = province_td.xpath(".//text()").get()
            province_text = re.sub(r"\s", "", province_text)
            if province_text:
                province = province_text
            if province == "其它":
                continue

            city_td = tds[1]
            city_links = city_td.xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()

                # print("省份:", province)
                # print("城市:", city)
                # print("城市链接:", city_url)

                #构建新房的url链接
                url_module = city_url.split("//")
                scheme = url_module[0]
                domain = url_module[1]

                if "bj." in domain:
                    newhouse_url = "http://newhouse.fang.com/house/s/"
                    esf_url = "http://esf.fang.com/"
                else:
                    newhouse_url = scheme + "//newhouse." + domain + "house/s/"
                    # 构建二手房url
                    esf_url = scheme + "//esf." + domain
                # print("城市:%s %s"%(province, city))
                # print("新房链接:%s"%(newhouse_url))
                # print("二手房链接:%s"% (esf_url))

                yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse, meta={'info': (province, city)})
                yield scrapy.Request(url=esf_url, callback=self.parse_esf, meta={"info": (province, city)})

    def parse_newhouse(self, response):
        provice, city = response.meta.get()
        pass

    def parse_esf(self, response):
        provice, city = response.meta.get()
