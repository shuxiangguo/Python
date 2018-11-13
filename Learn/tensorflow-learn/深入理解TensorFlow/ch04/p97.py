import tensorflow as tf
# 创建变量W
W = tf.Variable(0.0, name='W')
double = tf.multiply(2.0, W)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # 循环4次加法赋值操作
    for i in range(4):
        sess.run(tf.assign_add(W, 1.0))
        print('W=%s, double=%s' % (sess.run(W), sess.run(double)))

