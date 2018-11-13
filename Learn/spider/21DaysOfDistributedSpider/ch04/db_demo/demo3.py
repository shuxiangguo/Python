# encoding: utf-8
"""
@author: shuxiangguo
@file: demo3.py
@time: 2018-11-03 22:32:55
"""

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='123456', database='cloud_study', port=3306)
cursor = conn.cursor()

sql = "delete from user where Id=1"
cursor.execute(sql)
conn.commit()

sql2 = "update user set password='11111' where Id = 3"
cursor.execute(sql2)
conn.commit()