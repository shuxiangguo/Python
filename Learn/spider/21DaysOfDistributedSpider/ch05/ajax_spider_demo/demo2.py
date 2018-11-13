# encoding: utf-8
"""
@author: shuxiangguo
@file: demo2.py
@time: 2018-11-06 12:06:52
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.douban.com/")

# remberme = driver.find_element_by_id('form_remember')
remberme = driver.find_element(By.ID, 'form_remember')
remberme.click()