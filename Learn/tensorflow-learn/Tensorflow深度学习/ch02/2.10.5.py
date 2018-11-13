# encoding: utf-8
"""
@author: shuxiangguo
@file: 2.10.5.py
@time: 2018-11-05 13:29:45
"""

import tensorflow as tf
import numpy as np

constantA = tf.constant([100.0])
constantB = tf.constant([300.0])
constantC = tf.constant([3.0])

sum_ = tf.add(constantA, constantB)
mul_ = tf.multiply(constantA, constantB)


# 取回
with tf.Session() as sess:
	print(constantA.get_shape())

	#取回操作run()函数
	result = sess.run([sum_, mul_])
	print(result)



a = 3
b = 2
x = tf.placeholder(tf.float32, shape=(a,b))
y = tf.add(x,x)

data = np.random.rand(a,b)
# 注入
with tf.Session() as sess1:
	print(sess1.run(y, feed_dict={x:data}))