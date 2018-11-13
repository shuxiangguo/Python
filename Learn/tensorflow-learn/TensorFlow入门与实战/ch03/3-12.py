# 模型的载入

import tensorflow as tf

v1 = tf.Variable(..., name="v1")
v2 = tf.Variable(..., name="v2")

init_op = tf.global_variables_initializer()

# 处理保存和装载参数的saver
saver = tf.train.Saver()

with tf.Session() as sess:
    # 载入模型
    # 载入模型会将之前保存到文件模型中的参数重新读入到对应的标量中
    # 这里需要确保之前保存模型中定义的参数的名字和目前要装载的参数的名字相同

    saver.restore(sess, "/tmp/model.ckpt")