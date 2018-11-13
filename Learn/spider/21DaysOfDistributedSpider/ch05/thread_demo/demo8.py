# encoding: utf-8
"""
@author: shuxiangguo
@file: demo8.py
@time: 2018-11-04 15:19:19
"""
from queue import Queue

import requests
import os
from lxml import etree
from urllib.request import urlretrieve
import re
import threading


class Producer(threading.Thread):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
	}

	def __init__(self, page_queue, img_queue, *args, **kwargs):
		super(Producer, self).__init__(*args, **kwargs)
		self.page_queue = page_queue
		self.img_queue = img_queue

	def run(self):
		while True:
			if self.page_queue.empty():
				break
			url = self.page_queue.get()
			self.parse_page(url)
	def parse_page(self, url):
		response = requests.get(url, headers=self.headers)
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
			self.img_queue.put((img_url, filename))


class Consumer(threading.Thread):
	def __init__(self, page_queue, img_queue, *args, **kwargs):
		super(Consumer, self).__init__(*args, **kwargs)
		self.page_queue = page_queue
		self.img_queue = img_queue

	def run(self):
		while True:
			if self.img_queue.empty() and self.page_queue.empty():
				break

			img_url, filename = self.img_queue.get()
			urlretrieve(img_url, './images/'+filename)
			print(filename + '下载完完成')



def main():
	page_queue = Queue(100)
	img_queue = Queue(1000)
	for x in range(1, 101):
		url = "https://www.doutula.com/photo/list/?page=%d"%x
		page_queue.put(url)

	for x in range(5):
		t = Producer(page_queue, img_queue)
		t.start()

	for x in range(5):
		t = Consumer(page_queue, img_queue)
		t.start()


if __name__ == '__main__':
    main()