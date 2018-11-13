# encoding: utf-8
"""
@author: shuxiangguo
@file: load_test.py
@time: 2018-11-03 00:35:31
"""

import json

with open('./book1.json', 'r', encoding='utf-8') as fp:
	books = json.load(fp)
	print(type(books))
	for book in books:
		print(type(book))
		print(book)