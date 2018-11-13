# encoding: utf-8
"""
@author: shuxiangguo
@file: demo2.py
@time: 2018-11-04 10:04:33
"""

import threading
import time

class CodingThread(threading.Thread):
	def run(self):
		for x in range(3):
			print('正在coding:%s' % x)
			print(threading.current_thread())
			time.sleep(1)


class DrawingThread(threading.Thread):
	def run(self):
		for x in range(3):
			print('正在drawing:%s' % x)
			time.sleep(1)


def main():
	t1 = CodingThread()
	t2 = DrawingThread()

	t1.start()
	t2.start()


if __name__ == '__main__':
    main()