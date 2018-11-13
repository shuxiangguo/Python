# encoding: utf-8
"""
@author: shuxiangguo
@file: baisibudeqijie.py
@time: 2018-11-05 19:45:30
"""

# 多线程爬取百思不得其姐 段子地址：http://www.budejie.com/text/
# 通过生产者和消费者模式将爬取到的内容保存到csv文件中

import threading
import csv
from queue import Queue
import os
import requests
from lxml import etree

# cnt记录一共爬取了多少条
cnt = 0

class Producer(threading.Thread):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
	}
	def __init__(self, page_queue, text_queue,*args, **kwargs):
		super(Producer, self).__init__(*args, **kwargs)
		self.page_queue = page_queue
		self.text_queue = text_queue

	def run(self):
		while True:
			if self.page_queue.empty():
				break
			url = self.page_queue.get()
			self.parse_page(url)
		print(cnt)

	def parse_page(self, url):
		global cnt
		response = requests.get(url, headers=self.headers)
		text = response.text
		html = etree.HTML(text)

		alist = html.xpath('//div[@class="j-r-list-c-desc"]/a')
		# print(alist)
		for a in alist:
			text_url = a.xpath('./@href')
			# print(text_url)
			text = a.xpath('./text()')
			cnt += 1
			# print(text)
			self.text_queue.put((text_url, text))


class Consumer(threading.Thread):
	def __init__(self, page_queue, text_queue, writer, *args, **kwargs):
		super(Consumer, self).__init__(*args, **kwargs)
		self.page_queue = page_queue
		self.text_queue = text_queue
		self.writer = writer

	def run(self):

		while True:
			if self.text_queue.empty() and self.page_queue.empty():
				break
			text_url, text = self.text_queue.get()
			self.writer.writerow((text, text_url))



def main():
	page_queue = Queue(100)
	text_queue = Queue(10000)

	csv_file = open('./duanzi.csv', 'a', encoding='utf-8')
	writer = csv.writer(csv_file)
	writer.writerow(('text', 'text_url'))

	for i in range(1, 90):
		url = "http://www.budejie.com/text/%d"%i
		page_queue.put(url)

	for i in range(5):
		producer = Producer(page_queue, text_queue)
		producer.start()

	for i in range(10):
		consumer = Consumer(page_queue, text_queue, writer)
		consumer.start()



if __name__ == '__main__':
    main()


