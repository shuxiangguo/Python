# encoding: utf-8
"""
@author: shuxiangguo
@file: csv_writer_test.py
@time: 2018-11-03 01:16:32
"""

import csv

def csv_writer():
	headers = ['Username', 'age', 'heigth']
	students = [
		('zhangsan', 20, 180),
		('lisi', 21, 187),
		('王五', 22, 178)
	]
	with open('./studnents.csv', 'w', encoding='utf-8', newline='') as fp:
		writer = csv.writer(fp)
		writer.writerow(headers)
		writer.writerows(students)


def csv_dict_writer():
	headers = ['username', 'age', 'height']
	students = [
		{'username':'张三', 'age': 20, 'height': 180},
		{'username': '李四', 'age': 22, 'height': 175},
		{'username': '王五', 'age': 24, 'height': 170}
	]

	with open('./students1.csv', 'w', encoding='utf-8', newline='') as fp:
		writer = csv.DictWriter(fp, headers)

		# 写入表头数据时，需要调用writeheader()方法
		writer.writeheader()
		writer.writerows(students)



def main():
	# csv_writer()
	csv_dict_writer()


if __name__ == '__main__':
    main()