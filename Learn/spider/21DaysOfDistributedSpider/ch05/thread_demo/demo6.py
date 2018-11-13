# encoding: utf-8
"""
@author: shuxiangguo
@file: demo6.py
@time: 2018-11-04 14:07:06
"""
from queue import Queue
import threading
import time

#q = Queue(4)
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print(q.qsize())
#
# print(q.empty())
# print(q.full())
# for i in range(4):
# 	print(q.get())

def set_value(q):
	index = 0
	while True:
		q.put(index)
		index += 1
		time.sleep(3)


def get_value(q):
	while True:
		print(q.get())


def main():
	q = Queue()
	t1 = threading.Thread(target=set_value, args=[q])
	t2 = threading.Thread(target=get_value, args=[q])
	t1.start()
	t2.start()


if __name__ == '__main__':
    main()