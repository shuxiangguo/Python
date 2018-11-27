# encoding: utf-8
"""
@author: shuxiangguo
@file: start.py
@time: 2018-11-27 21:16:01
"""

from scrapy import cmdline

cmdline.execute("scrapy crawl httpbin".split())