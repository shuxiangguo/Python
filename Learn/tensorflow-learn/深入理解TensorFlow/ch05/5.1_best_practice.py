from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

flags = tf.app.flags
flags.DEFINE_string("data_dir", "/tmp/mnist-data", "Directory for  storing mnist")
flags.DEFINE_float("leaning_rate", 0.5, "Learning rate")

FLAGS = flags.FLAGS

def main():
    # 创建MNIST数据集实例
    mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
    # 创建模型
    x = tf.placeholder(tf.float32, [None, 784]) # 图形数据
    W = tf.Variable(tf.zeros[784, 10]) # 模型权重
    b = tf.Variable(tf.zeros[10]) # 模型偏置
    Y= tf.matmul(x, W) + b
    y_ = tf.placeholder(tf.float32, [None, 10]) # 图形标签

    # 使用交叉熵作为损失值
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(label=y_, logits=y))
    # 创建梯度下降优化器
    optimizer = tf.train.GradientDescentOptimizer(FLAGS.learning_rate)
    # 定义单步训练操作
    train_op = optimizer.minimize(cross_entropy)