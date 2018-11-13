# encoding: utf-8
"""
@author: shuxiangguo
@file: start.py
@time: 2018-11-13 19:06:01
"""

from scrapy import cmdline

cmdline.execute("scrapy crawl qsbk_spider".split())