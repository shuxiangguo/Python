# encoding: utf-8
"""
@author: shuxiangguo
@file: words_spider.py
@time: 2018-11-02 21:24:57
"""

import requests
import re

def parse_page(url):
	header = {
		'Uesr-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
	}
	response = requests.get(url, header)
	text = response.text

	contents = re.findall(r'<div class="content">.*?<span>(.*?)</span>', text, re.S)
	duanzi = []
	for content in contents:
		x = re.sub(r'<.*?>', '', content)
		duanzi.append(x.strip())
		print(x.strip())
		print('='*40)
	print(contents)


def main():
	for x in range(1, 11):
		url = "https://www.qiushibaike.com/text/page/%s/"%x
		parse_page(url)

if __name__ == '__main__':
    main()