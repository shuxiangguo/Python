# 指定GPU设备


import tensorflow as tf
import os
os.environ['CUDA_VISIBLE_DEVICES'] = "0"



with tf.device("/cpu:0"):
    v1 = tf.constant(1)
    v2 = tf.constant(2)

with tf.device("/gpu:0"):
    v3 = tf.constant(3)
    v4 = tf.constant(4)

with tf.device("gpu:1"):
    v5 = tf.constant(5)


with tf.Session(config=tf.ConfigProto(log_device_placement=True, allow_soft_placement=True)) as sess:
    print(sess.run(v5))