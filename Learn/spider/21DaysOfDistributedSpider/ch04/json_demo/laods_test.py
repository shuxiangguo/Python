# encoding: utf-8
"""
@author: shuxiangguo
@file: laods_test.py
@time: 2018-11-03 00:29:27
"""

import json
# json.laods函数将json格式的字符串转换成python对象
json_str = '[{"title": "钢铁是怎样炼成的", "price": 9}, {"title": "红楼梦", "price": 20}]'
books = json.loads(json_str)
print(type(books))
print(books)
for book in books:
	print(book)