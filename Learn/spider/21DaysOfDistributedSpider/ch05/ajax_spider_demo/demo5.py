# encoding: utf-8
"""
@author: shuxiangguo
@file: demo5.py
@time: 2018-11-06 14:04:23
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 获取所有cookie
for cookie in driver.get_cookies():
	print(cookie)

print("="*20)

# 获取某个cookie
print(driver.get_cookie("domain"))

# driver.delete_all_cookies()
