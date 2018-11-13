import tensorflow as tf

# 导入数据集
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 变量
batch_size = 100

# 训练的x(image), y(label)
# x = tf.Variable()
# y = tf.Variable()

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

# 模型权重
# [55000, 784] * W  = [55000, 10]
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 用softmax构建逻辑回归模型
pred = tf.nn.softmax(tf.matmul(x, W) + b)

# 损失函数
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), 1))

# 梯度下降
optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(cost)


# 初始化所有变量
init = tf.global_variables_initializer()


# 加载session图
with tf.Session() as sess:
	sess.run(init)

	# 开始训练
	for epoch in range(25):
		avg_cost = 0
		total_batch = int(mnist.train.num_examples / batch_size)
		for i in range(total_batch):
			batch_xs, batch_ys = mnist.train.next_batch(batch_size)
			sess.run(optimizer, {x: batch_xs, y: batch_ys})

			# 计算损失平均值
			avg_cost += sess.run(cost, {x: batch_xs, y: batch_ys}) / total_batch

		if (epoch + 1) % 5 == 0:
			print("Epoch: ", '%04d' % (epoch+1), "cost = ", "{:.9f}".format(avg_cost))

	print("运行完成")

	# 测试正确率
	correct = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
	accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))
	print("正确率:", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))

