# encoding: utf-8
"""
@author: shuxiangguo
@file: demo6.py
@time: 2018-11-06 18:49:47
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 执行js代码
driver.execute_script("window.open('https://www.douban.com')")

print(driver.current_url)

driver.switch_to_window(driver.window_handles[1])
print(driver.current_url)