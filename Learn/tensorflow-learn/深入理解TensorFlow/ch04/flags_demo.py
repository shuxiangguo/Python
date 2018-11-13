import tensorflow as tf
flags = tf.app.flags
flags.DEFINE_string("data_dir", "/tmp/mnist-data", "Directory for storing mnist data")
FLAGS = flags.FLAGS # 将解析成功的参数保存到flags.FLAGS名字空间中
def main(_):
    print(FLAGS.data_dir)
if __name__ == '__main__':
    tf.app.run()