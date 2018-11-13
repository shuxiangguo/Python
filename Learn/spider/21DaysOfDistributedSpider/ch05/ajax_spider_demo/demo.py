# encoding: utf-8
"""
@author: shuxiangguo
@file: demo.py
@time: 2018-11-06 02:32:51
"""

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
input_tag = driver.find_element_by_class_name('s_ipt')

# 使用send_keys()方法向表单发送数据
input_tag.send_keys('hello world')
time.sleep(3)

# clear()方法清除输入
input_tag.clear()