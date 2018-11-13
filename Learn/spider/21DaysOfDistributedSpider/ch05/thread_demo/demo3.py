# encoding: utf-8
"""
@author: shuxiangguo
@file: demo3.py
@time: 2018-11-04 10:09:34
"""

import threading

VALUE = 0
gLock = threading.Lock()

def add_value():
	global VALUE
	gLock.acquire()
	for x in range(1000000):
		VALUE += 1
	gLock.release()
	print('value: %d'%VALUE)


def main():
	for x in range(2):
		t = threading.Thread(target=add_value)
		t.start()


if __name__ == '__main__':
	main()