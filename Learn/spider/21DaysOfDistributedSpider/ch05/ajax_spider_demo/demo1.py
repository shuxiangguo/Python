# encoding: utf-8
"""
@author: shuxiangguo
@file: demo1.py
@time: 2018-11-06 01:43:55
"""

# 测试selenium的函数
from selenium import webdriver
from lxml import etree

driver = webdriver.Chrome()

# html = etree.HTML(driver.page_source)
# html.xpath("")


driver.get('https://www.baidu.com')
input_tags = driver.find_element_by_class_name('s_ipt')
input_tags.send_keys('python')

# 1.如果只是想要解析网页中的数据，那么推荐将网页源代码扔给lxml来解析，因为lxml底层用的是C语言，所以解释效率会更高

# 2.如果想要对元素进行一些操作，如给文本框输入值，或者是点击某个按钮，那么必须使用selenium给我们提供的查找元素的方法，因为方法send_keys()只在这些下面可用。