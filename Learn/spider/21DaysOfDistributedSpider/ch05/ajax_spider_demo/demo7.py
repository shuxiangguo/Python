# encoding: utf-8
"""
@author: shuxiangguo
@file: demo7.py
@time: 2018-11-06 16:07:37
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.douban.com")

# driver.implicitly_wait(10)

element = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.ID, 'form_email'))
)
print(element)