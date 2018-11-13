# encoding: utf-8
"""
@author: shuxiangguo
@file: demo1.py
@time: 2018-11-08 14:45:45
"""

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
image = Image.open('1.png')
text = pytesseract.image_to_string(image, lang='chi_sim')
print(text)