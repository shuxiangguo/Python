# encoding: utf-8
"""
@author: shuxiangguo
@file: demo8.py
@time: 2018-11-06 21:10:12
"""

# selenium中添加代理
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://117.191.11.71:80")
driver = webdriver.Chrome(chrome_options=options)

driver.get('http://httpbin.org/ip')