# encoding: utf-8
"""
@author: shuxiangguo
@file: demo7.py
@time: 2018-11-04 14:33:23
"""

import requests
import os
from lxml import etree
from urllib.request import urlretrieve
import re


def parse_page(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
	}
	response = requests.get(url, headers=headers)
	text = response.text
	html = etree.HTML(text)
	images = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
	for image in images:
		img_url = image.get('data-original')[:-4]
		print(img_url)
		alt = image.get('alt')
		alt = re.sub(r'[\?？\.，。！!]', "", alt)
		suffix = os.path.splitext(img_url)[1]
		# print(suffix)
		filename = alt + suffix
		print(filename)
		urlretrieve(img_url, './images/' + filename)



def main():
	for x in range(1, 101):
		url = "https://www.doutula.com/photo/list/?page=%d"%x
		parse_page(url)


if __name__ == '__main__':
    main()