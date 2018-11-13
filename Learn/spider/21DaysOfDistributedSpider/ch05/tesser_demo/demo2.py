# encoding: utf-8
"""
@author: shuxiangguo
@file: demo2.py
@time: 2018-11-08 15:00:17
"""
# 利用tesseract识别图形验证码

import pytesseract
from PIL import Image
from urllib import request
import time

def main():
	pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
	url = "https://v4.passport.sohu.com/i/captcha/picture?pagetoken=1541661770041&random=passport403_sdk1541661770039"

	# 将验证码图片保存到本地，然后用tesseract去识别，直到成功。
	while True:

		# 注意图片保存的格式，一开始保存成.png报错：
		# OSError: cannot identify image file

		request.urlretrieve(url, "a.jpg")
		image = Image.open("a.jpg")
		text = pytesseract.image_to_string(image)
		print(text)
		time.sleep(2)


if __name__ == '__main__':
    main()
