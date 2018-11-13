# 使用Saver保存模型参数
import tensorflow as tf
# 创建变量W
W = tf.Variable(0.0, name='W')
double = tf.multiply(2.0, W)

# 创建Saver
saver = tf.train.Saver({'weights': W})
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(4):
        sess.run(tf.assign_add(W, 1.0))
        # 存储变量W
        saver.save(sess, '/tmp/summary/test.ckpt')
