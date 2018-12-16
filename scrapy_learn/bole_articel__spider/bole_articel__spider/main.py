# encoding: utf-8
"""
@author: shuxiangguo
@file: main.py
@time: 2018-12-16 12:34:25
"""

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole"])
