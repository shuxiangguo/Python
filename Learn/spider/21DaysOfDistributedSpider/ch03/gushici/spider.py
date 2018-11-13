# encoding: utf-8
"""
@author: shuxiangguo
@file: spider.py
@time: 2018-11-02 19:24:01
"""

import requests
import re

def parse_page(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
	}

	response = requests.get(url, headers)
	text = response.text
	titles = re.findall(r'<div\sclass="cont".*?<b>(.*?)</b>', text, re.DOTALL)
	# print(titles)
	dynasties = re.findall(r'<p\sclass="source".*?<a.*?>(.*?)</a>', text, re.DOTALL)
	# print(dynasties)
	authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
	# print(authors)
	contents_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>', text, re.DOTALL)

	contents = []
	for content in contents_tags:
		x = re.sub(r'<.*?>', "", content)
		contents.append(x.strip())

	poems = []
	for value in zip(titles, dynasties, authors, contents):
		title, dynasty, author, content = value
		poem = {
			'title': title,
			'dynasty': dynasty,
			'author': author,
			'content': content
		}

		poems.append(poem)
	for x in poems:
		print(x)
		print('#'*40)




def main():
	for x in range(1, 11):
		url = "https://www.gushiwen.org/default_%s.aspx"%x
		parse_page(url)


if __name__ == '__main__':
	main()

