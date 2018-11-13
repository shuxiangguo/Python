# encoding: utf-8
"""
@author: shuxiangguo
@file: demo4.py
@time: 2018-11-04 11:00:28
"""

import threading
import random
import time

gmoney = 1000
gTotalTimes = 10
gTimes = 0
gLock = threading.Lock()


class Producer(threading.Thread):
	def run(self):
		global gmoney
		global gTimes
		while True:
			money = random.randint(100, 1000)
			gLock.acquire()
			if gTimes >= gTotalTimes:
				gLock.release()
				break
			gmoney += money
			print('%s生产了%d元钱，剩余%d元钱'%(threading.current_thread(), money, gmoney))
			gTimes += 1
			gLock.release()
			time.sleep(0.5)


class Consumer(threading.Thread):
	def run(self):
		global gmoney
		while True:
			money = random.randint(100, 1000)
			gLock.acquire()
			if gmoney > money:
				gmoney -= money
				print('%s消费了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gmoney))
			else:
				if gTimes >= gTotalTimes:
					gLock.release()
					break
				print('%s准备消费%d元钱,剩余%d元钱，不足'%(threading.current_thread(), money, gmoney))
			gLock.release()
			time.sleep(0.5)


def main():
	for i in range(5):
		t = Producer()
		t.start()

	for i in range(3):
		t = Consumer()
		t.start()


if __name__ == '__main__':
    main()