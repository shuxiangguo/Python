# encoding: utf-8
"""
@author: shuxiangguo
@file: demo1.py
@time: 2018-11-04 09:08:13
"""

import pymongo

# 获取连接Mongodb的对象
client = pymongo.MongoClient('localhost', port=27017)

# 获取数据库
db = client.zhihu

# 获取数据库中的集合collection
collection = db.qa


# 插入数据
# collection.insert_many([
# 	{
# 		'username': "aaa",
# 		'age': 18
# 	},
# 	{
# 		'username': 'bbb',
# 		'age': 20
# 	}
# ])

# 查找数据
# # find获取集合中所有数据
# cursor = collection.find()
# for x in cursor:
# 	print(x)

# 获取集合中一条数据
# result = collection.find_one({'age': 18})
# print(result)

# 更新数据
# collection.update_many({'username': 'aaa'}, {'$set': {'username': 'bbb'}})

# 删除数据
# collection.delete_one({'username': 'bbb'})
collection.delete_many({'username': 'bbb'})