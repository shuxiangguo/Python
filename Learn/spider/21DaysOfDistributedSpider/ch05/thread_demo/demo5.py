# encoding: utf-8
"""
@author: shuxiangguo
@file: demo5.py
@time: 2018-11-04 13:39:54
"""


import threading
import random
import time

gmoney = 1000
gTotalTimes = 10
gTimes = 0
gCondition = threading.Condition()


class Producer(threading.Thread):
	def run(self):
		global gmoney
		global gTimes
		while True:
			money = random.randint(100, 1000)
			gCondition.acquire()
			if gTimes >= gTotalTimes:
				gCondition.release()
				break
			gmoney += money
			print('%s生产了%d元钱，剩余%d元钱'%(threading.current_thread(), money, gmoney))
			gTimes += 1
			gCondition.notify_all()
			gCondition.release()
			time.sleep(0.5)


class Consumer(threading.Thread):
	def run(self):
		global gmoney
		while True:
			money = random.randint(100, 1000)
			gCondition.acquire()
			while gmoney < money:
				if gTimes >= gTotalTimes:
					gCondition.release()
					return
				else:
					print('%s准备消费%d元钱,剩余%d元钱，不足' % (threading.current_thread(), money, gmoney))
				gCondition.wait()
			gmoney -= money
			print("%s消费了%d元钱，剩余%d元钱"%(threading.current_thread(), money, gmoney))
			gCondition.release()
			time.sleep(0.5)


def main():
	for i in range(3):
		t = Consumer()
		t.start()


	for i in range(5):
		t = Producer()
		t.start()



if __name__ == '__main__':
    main()