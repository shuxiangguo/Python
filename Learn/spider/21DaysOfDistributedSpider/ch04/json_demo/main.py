# encoding: utf-8
"""
@author: shuxiangguo
@file: main.py
@time: 2018-11-02 23:29:14
"""

import json

books = [
	{
		'title': '钢铁是怎样炼成的',
		'price': 9
	},
	{
		'title': '红楼梦',
		'price': 20
	}
]

# json.dumps函数将python对象转换成json字符串
# 只有基本数据类型才能转换成json格式的字符串
json_str = json.dumps(books, ensure_ascii=False)
print(type(json_str))
print(json_str)

with open('book.json', 'w', encoding='utf-8') as fp:
	fp.write(json_str)

with open('book1.json', 'w', encoding='utf-8') as fp:
	json.dump(books, fp, ensure_ascii=False)