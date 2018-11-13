# encoding: utf-8
"""
@author: shuxiangguo
@file: spider.py
@time: 2018-10-29 21:45: 25
"""

import requests
from lxml import etree

BASE_DOMAIN = 'http://dytt8.net'

proxy = {
	'http': '39.137.2.194:8080'
}
HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
	'Referer': 'https://movie.douban.com/'
}


def get_detail_urls(url):
	response = requests.get(url, headers=HEADERS, proxies=proxy)
	# response.text
	# response.content
	# requests库，默认会使用自己猜测的解码方式将抓取下来的网页进行解码，
	# 然后存储到reponse.text属性上，在电影天堂的网页中，因为编码方式requests猜错了，
	# 所以会产生乱码
	text = response.text
	html = etree.HTML(text)

	detail_urls = html.xpath("//table[@class='tbspan']//a/@href")

	# lambda表达式
	detail_urls = map(lambda url:BASE_DOMAIN+url, detail_urls)
	return detail_urls

def spider():
	base_url = 'http://dytt8.net/html/gndy/dyzz/list_23_{}.html'
	movies = []
	for x in range(1, 8):
		# 第一个for循环用来控制一共有7页
		# print("="*20)
		# print(x)
		url = base_url.format(x)
		detail_urls = get_detail_urls(url)
		for detail_url in detail_urls:
			# 这个for循环用来遍历每页所有电影详情页url
			# print(detail_url)
			movie = parse_detail_page(detail_url)
			movies.append(movie)
			print(movies)




def parse_detail_page(url):
	movie = {}
	response = requests.get(url, headers=HEADERS)
	text = response.content.decode('gbk')
	html = etree.HTML(text)
	title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
	movie['title'] = title

	zoomE = html.xpath("//div[@id='Zoom']")[0]
	imgs = zoomE.xpath(".//img/@src")
	cover = imgs[0]
	movie['cover'] = cover
	if len(imgs) > 1:
		screenshot = imgs[1]
		movie['screenshot'] = screenshot

	def parse_info(info, rule):
		return info.replace(rule, "")

	infos = zoomE.xpath(".//text()")
	for index, info in enumerate(infos):

		if info.startswith('◎年　　代'):
			info = parse_info(info, "◎年　　代")
			movie['year'] = info
		elif info.startswith('◎产　　地'):
			info = parse_info(info, "◎产　　地")
			movie['place'] = info
		elif info.startswith('◎类　　别'):
			info = parse_info(info, "◎类　　别")
			movie['category'] = info
		elif info.startswith('◎豆瓣评分'):
			info = parse_info(info, '◎豆瓣评分')
			movie['douban_rating'] = info
		elif info.startswith('◎片　　长'):
			info = parse_info(info, '◎片　　长')
			movie['duration'] = info
		elif info.startswith('◎导　　演'):
			info = parse_info(info, '◎导　　演')
			movie['director'] = info
		elif info.startswith('◎主　　演'):
			info = parse_info(info, '◎主　　演')
			actors = [info]
			for x in range(index+1, len(infos)):
				actor = infos[x].strip()
				if actor.startswith('◎'):
					break
				actors.append(actor)
			movie['acotrs'] = actors
		elif info.startswith('◎简　　介 '):
			info = parse_info(info, '◎简　　介 ')
			for x in range(index+1, len(infos)):
				profile = infos[x].strip()
				if profile.startswith("【下载地址】"):
					break
			movie['profile'] = movie
	download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
	movie['download_url'] = download_url
	return movie


if __name__ == '__main__':
	spider()


## 学堂在线



