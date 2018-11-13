# encoding: utf-8
"""
@author: shuxiangguo
@file: laods_test.py
@time: 2018-10-31 02:01:34
"""
import bs4
html = """

"""

bs = bs4.BeautifulSoup(html, 'lxml')
print(bs.prettify())