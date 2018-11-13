# 模型的保存

import tensorflow as tf

v1 = tf.Variable(..., name="v1")
v2 = tf.Variable(..., name="v2")
step = 0

init_op = tf.global_variables_initializer()

# 定义保存参数的saver
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init_op)
    while True:
        step += 1

        # 接下去做模型的训练过程
        pass
        if step % 1000 == 0:
            # 保存模型参数
            save_path = saver.save(sess, "./model/model.ckpt", global_step=step)
            print("Model saved in file:%s" % save_path)
