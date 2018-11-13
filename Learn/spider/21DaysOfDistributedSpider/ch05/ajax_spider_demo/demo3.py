# encoding: utf-8
"""
@author: shuxiangguo
@file: demo3.py
@time: 2018-11-06 13:51:36
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")


input_tag = driver.find_element_by_id('kw')
submit_tag = driver.find_element_by_id('su')

action = ActionChains(driver)
action.move_to_element(input_tag)
action.send_keys_to_element(input_tag, "python")
action.move_to_element(submit_tag)
action.click(submit_tag)
action.perform()