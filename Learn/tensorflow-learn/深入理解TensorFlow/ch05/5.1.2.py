import tensorflow as tf
# 创建数据流图g1
g1 = tf.Graph()
with g1.as_default():
    a = tf.Variable(0, name='a')
    assert a.graph is g1

with tf.Graph().as_default() as g2:
    b = tf.Variable(0, name='b')
    assert b.graph == g2
    