# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from PIL import Image


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login']
    url = 'https://accounts.douban.com/login'
    profile_url = 'https://www.douban.com/people/156908540/'
    edit_signatur_url = 'https://www.douban.com/j/people/156908540/edit_signature'


    def parse(self, response):
        formdata = {
            'source': "index_nav",
            'redir': "https://www.douban.com/",
            'form_email': "18756938278",
            'form_password': "lsg1234567",
            'remember': 'on',
            'login': '登录'
        }

        captcha_url = response.css("img#captcha_image::attr(src)").get()
        if captcha_url:
            captcha = self.recgonize_captcha(captcha_url)
            formdata['captcha-solution'] = captcha
            captcha_id = response.xpath('//input[@name="captcha-id"]/@value').get()
            formdata['captcha-id'] = captcha_id
        yield scrapy.FormRequest(url=self.url, formdata=formdata, callback=self.parse_after_login)

    def parse_after_login(self, response):
        print(response.url)
        if response.url == 'https://www.douban.com/':
            yield scrapy.Request(self.profile_url, callback=self.parse_profile)
            print('登录成功')
        else:
            print('登录失败')

    def parse_profile(self, response):
        print(response.url)
        if response.url == self.profile_url:
            ck = response.xpath('//input[@name="ck"]//@value').get()
            print(ck)
            formdata = {
                'ck': ck,
                'signature': 'I am shuxiangguo'
            }
            yield scrapy.FormRequest(url=self.edit_signatur_url, formdata=formdata)
        else:
            print('没有进入个人中心')



    def recgonize_captcha(self, captcha_url):
        urllib.request.urlretrieve(captcha_url, 'captcha.png')
        image = Image.open('captcha.png')
        image.show()
        captcha = input('请输入验证码:')
        return captcha
