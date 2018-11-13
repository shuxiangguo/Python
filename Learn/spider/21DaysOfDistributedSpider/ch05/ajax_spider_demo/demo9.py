# encoding: utf-8
"""
@author: shuxiangguo
@file: demo9.py
@time: 2018-11-06 22:52:57
"""

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

driver = webdriver.Chrome()
driver.get("http://www.douban.com")

div_tag = driver.find_element_by_id('anony-nav')
driver.save_screenshot('./douban.png')
print(type(div_tag))