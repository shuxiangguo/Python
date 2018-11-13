# encoding: utf-8
"""
@author: shuxiangguo
@file: spider.py
@time: 2018-11-02 03:33:44
"""
import requests
from bs4 import BeautifulSoup

def parse_page(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
	}

	response = requests.get(url, headers=headers)
	print(response.text)


def main():
	url = ""