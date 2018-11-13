import tensorflow as tf
import numpy as np

# 占位符，适用于不知道具体参数的时候
x = tf.placeholder(tf.float32, shape=(4, 4))
y = tf.add(x, x)
# [1,  32, 44, 56]
# [89, 12, 90, 33]
# [35, 69, 1,  10]
argmax_paramter = tf.Variable([[1, 32, 44, 56], [89, 12, 90, 33], [35, 69, 1, 10]])

# 最大列索引
argmax_0 = tf.argmax(argmax_paramter, 0)
# 最大行索引
argmax_1 = tf.argmax(argmax_paramter, 1)

# 平均数
reduce_0 = tf.reduce_mean(argmax_paramter, reduction_indices=0)
reduce_1 = tf.reduce_mean(argmax_paramter, reduction_indices=1)

# 相等
equal_0 = tf.equal(1, 2)
equal_1 = tf.equal(2, 2)

# 类型转换     ??????????????????????
cast_0 = tf.cast(equal_0, tf.int32)
cast_1 = tf.cast(equal_1, tf.float32)

with tf.Session() as sess:
	init = tf.global_variables_initializer();
	sess.run(init)

	rand_array = np.random.rand(4, 4)
	print(sess.run(y, feed_dict={x: rand_array}))

	print("argmax_0:", sess.run(argmax_0))
	print("argmax_1:", sess.run(argmax_1))
	print("reduce_0:", sess.run(reduce_0))
	print("reduce_1:", sess.run(reduce_1))
	print("equal_0:", sess.run(equal_0))
	print("equal_1:", sess.run(equal_1))
	print("cast_0:", sess.run(cast_0))
	print("cast_1:", sess.run(cast_1))