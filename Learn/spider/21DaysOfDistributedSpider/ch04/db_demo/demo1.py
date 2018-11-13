# encoding: utf-8
"""
@author: shuxiangguo
@file: demo1.py
@time: 2018-11-03 03:28:40
"""

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='123456', database='cloud_study', port=3306)
cursor = conn.cursor()

# insert into user(Id, userName, password,account) values(7, 'sxg', 'sss', 888)
sql = "insert into user(Id, userName, password,account) values(null, %s, %s, %s)"

username = "shuxiang"
password = "1211"
account = 123
cursor.execute(sql, (username, password, account))

conn.commit()

conn.close()