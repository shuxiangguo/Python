# encoding: utf-8
"""
@author: shuxiangguo
@file: 2.13.py
@time: 2018-11-05 13:54:07
"""

import tensorflow as tf
import numpy as np

input_value = tf.constant(0.5, name="input_value")
weight = tf.Variable(1.0, name="weight")
expected_output = tf.constant(0.0, name="expected_output")

model = tf.multiply(input_value, weight, name="model")
loss_function = tf.pow(expected_output-model, 2, name="loss_function")

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.025).minimize(loss_function)

for value in [input_value, weight, expected_output, model, loss_function]:
	tf.summary.scalar(value.op.name, value)
summaries = tf.summary.merge_all()

sess = tf.Session()
summary_writer = tf.summary.FileWriter('log_simple_stats', sess.graph)
sess.run(tf.global_variables_initializer())
for i in range(100):
	summary_writer.add_summary(sess.run(summaries), i)
	sess.run(optimizer)