# 使用Saver.restore方法从checkpoint文件中恢复变量值
import tensorflow as tf
# 创建变量W
W = tf.Variable(0.0, name='weights')
double = tf.multiply(2.0, W)
# 创建Saver
saver = tf.train.Saver()
with tf.Session() as sess:
    # 恢复变量W的值
    saver.restore(sess, '/tmp/summary/test.ckpt')
    print('restored:W=%s' % sess.run(W))
    for i in range(4):
        sess.run(tf.assign_add(W, 1.0))
        print('W=%s, double=%s' % (sess.run(W), sess.run(double)))