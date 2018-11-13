# encoding: utf-8
"""
@author: shuxiangguo
@file: ajax_spider.py
@time: 2018-11-05 22:35:03
"""
# 使用selenium和chromedriver模拟浏览器行为

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# print(driver.page_source)
time.sleep(5)

# driver.close()
driver.quit()