# encoding: utf-8
"""
@author: shuxiangguo
@file: demo2.py
@time: 2018-11-03 22:19:44
"""

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='123456', database='cloud_study', port=3306)
cursor = conn.cursor()
sql = "select userName, password from user"
cursor.execute(sql)

def test_fetchone():
	# test fetchone
	while True:
		result = cursor.fetchone()
		if result:
			print(result)
		else:
			break


def test_fetchall():
	results = cursor.fetchall()
	for result in results:
		print(result)


def test_fetchmany():
	results = cursor.fetchmany(2)
	print(type(results))
	for result in results:
		print(result)

def main():
	# test_fetchall()
	test_fetchmany()
	conn.close()


if __name__ == '__main__':
    main()