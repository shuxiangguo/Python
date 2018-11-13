# encoding: utf-8
"""
@author: shuxiangguo
@file: demo1.py
@time: 2018-11-03 00:54:54
"""

import csv

def read_csv_to_list():
	with open('./supplier_data.csv', 'r', encoding='utf-8') as fp:
		reader = csv.reader(fp)
		next(reader)

		for thing in reader:
			supplier_name = thing[0]
			price = thing[3]
			thing_dict = {
				'supplier_name': supplier_name,
				'price': price
			}
			print(thing_dict)


def read_csv_to_dict():
	with open('./supplier_data.csv', 'r', encoding='utf-8') as fp:

		# 使用DictReader创建的reader对象不会包含标题行数据
		# reader是一个迭代器，遍历这个迭代器，返回的是一个字典
		reader = csv.DictReader(fp)

		for thing in reader:
			print(thing['Cost'])



def main():
	# read_csv_to_list()
	read_csv_to_dict()

if __name__ == '__main__':
    main()