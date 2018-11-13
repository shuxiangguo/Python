# encoding: utf-8
"""
@author: shuxiangguo
@file: main.py
@time: 2018-10-29 16:08: 31
"""

import requests
from lxml import etree

# 1.将目标网站上的页面抓取下来
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
	'Referer': 'https://movie.douban.com/'
}

url = 'https://movie.douban.com/cinema/nowplaying/chizhou/'
response = requests.get(url, headers=headers)
text = response.text

# 2.将抓取下来的数据根据一定的规则进行提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul, encoding='utf-8').decode('utf-8'))

lis = ul.xpath("./li")
movies = []
for li in lis:
	# print(etree.tostring(li, encoding='utf-8').decode('utf-8'))
	title = li.xpath("@data-title")[0]
	score = li.xpath("@data-score")[0]
	duration = li.xpath("@data-duration")[0]
	region = li.xpath("@data-region")[0]
	director = li.xpath("@data-director")[0]
	actors = li.xpath("@data-actors")[0]
	img = li.xpath(".//img/@src")[0]

	movie = {
		'title': title,
		'score': score,
		'duration': duration,
		'region': region,
		'director': director,
		'actors': actors,
		'img': img
	}
	movies.append(movie)

print(movies)


