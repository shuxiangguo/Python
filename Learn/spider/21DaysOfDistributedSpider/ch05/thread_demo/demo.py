# encoding: utf-8
"""
@author: shuxiangguo
@file: demo.py
@time: 2018-11-04 09:52:48
"""

import time
import threading

# def coding():
# 	for x in range(3):
# 		print('正在coding:%s'%x)
# 		time.sleep(1)
#
#
# def draw():
# 	for x in range(3):
# 		print('正在drawing:%s'%x)
# 		time.sleep(1)
#
#
# def main():
# 	coding()
# 	draw()
#
#
# if __name__ == '__main__':
#     main()
#
#

# 采用多线程方式

def coding():
	for x in range(3):
		print('正在coding:%s'%x)
		print(threading.current_thread())
		time.sleep(1)


def draw():
	for x in range(3):
		print('正在drawing:%s'%x)
		time.sleep(1)


def main():
	t1 = threading.Thread(target=coding)
	t2 = threading.Thread(target=draw)

	t1.start()
	t2.start()

	print(threading.enumerate())


if __name__ == '__main__':
    main()