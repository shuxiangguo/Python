from generate import gen_captcha_text_and_image
from generate import number
# from Gen_captcha import ALPHABET
# from Gen_captcha import alphabet

import numpy as np
import tensorflow as tf

# text, image = gen_captcha_text_and_image()
# print("图像尺寸为：", image.shape) 60 * 160 * 3
# print(len(text)) 4
IMAGE_HEIGHT = 60
IMAGE_WIDTH = 160
Length = 4
Char_Numbers = 10 # 26 * 2 + 10 = 62

lr = 0.001

# 图片转灰色，颜色不起作用
def convert2grey(img):
    if len(img.shape) > 2:
        gray = np.mean(img, -1)
        # 上面的转法较快，正规转法如下
        # r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
        # gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray
    else:
        return img

# 文本结果转向量
def text2vec(txt):
    vector= np.zeros(Length * Char_Numbers) # (0,248)
    for i, c in enumerate(txt):
        k = ord(c) - 48
        if k > 9:
            k = ord(c) - 55
            if k > 35:
                k = ord(c) - 61
        idx = i * Char_Numbers + k
        vector[idx] = 1
    return vector

def init_weights(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))

def model(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden):
    x = tf.reshape(X, [-1, IMAGE_HEIGHT, IMAGE_WIDTH, 1])

    l1a = tf.nn.relu(tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')) #l1a shape(?,60,160,32)
    l1 = tf.nn.max_pool(l1a, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME')# l1 shape(?, 30, 80, 32)
    l1 = tf.nn.dropout(l1, p_keep_conv)

    l2a = tf.nn.relu(tf.nn.conv2d(l1, w2, strides=[1, 1, 1, 1], padding='SAME')) # l2a shape(?, 30, 80, 64)
    l2 = tf.nn.max_pool(l2a, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME') # l2 shape(?, 15, 40, 64)
    l2 = tf.nn.dropout(l2, p_keep_conv)

    l3a = tf.nn.relu(tf.nn.conv2d(l2, w3, strides=[1, 1, 1, 1], padding='SAME')) #l3a shape(?, 15, 40, 128)
    l3 = tf.nn.max_pool(l3a, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME') #l3 shape(?, 8, 20, 128)
    l3  = tf.nn.dropout(l3, p_keep_conv)

    l3 = tf.reshape(l3, [-1, w4.get_shape().as_list()[0]]) # reshape to (?, 20480)
    l4 = tf.nn.relu(tf.matmul(l3, w4))
    l4 = tf.nn.dropout(l4, p_keep_hidden) # l4 shape(?, 625)

    pyx = tf.matmul(l4, w_o)

    return pyx #pyx shape(?, 40)


def get_batch(batchsize = 128):
    batch_x = np.zeros([batchsize, IMAGE_HEIGHT * IMAGE_WIDTH ])   #(128, 60*160=9600)
    batch_y = np.zeros([batchsize, Length * Char_Numbers]) # (128, 4*(26+26+10)=248)

    for i in range(batchsize):
        text, image = gen_captcha_text_and_image()
        image = convert2grey(image)

        batch_x[i:] = image.flatten() / 255
        batch_y[i:] = text2vec(text)

    return batch_x, batch_y # (128, 9600), (128, 40)


X = tf.placeholder("float", [None, IMAGE_HEIGHT * IMAGE_WIDTH ]) # [None, 9600]
Y = tf.placeholder("float", [None, Length * Char_Numbers]) # [None, 248]


w = init_weights([3, 3, 1, 32])       # 3x3x1 conv, 32 outputs
w2 = init_weights([3, 3, 32, 64])     # 3x3x32 conv, 64 outputs
w3 = init_weights([3, 3, 64, 128])    # 3x3x32 conv, 128 outputs
w4 = init_weights([128 * 8 * 20, 625]) # FC 128 * 8 * 20 inputs, 625 outputs
w_o = init_weights([625, Length * Char_Numbers])

p_keep_conv = tf.placeholder("float")
p_keep_hidden = tf.placeholder("float")
py_x = model(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden)

# # cost
cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=py_x, labels=Y))
tf.summary.scalar("cost", cost)

# # optimizer
# train_op = tf.train.RMSPropOptimizer(lr, 0.9).minimize(cost)
# train_op = tf.train.GradientDescentOptimizer(learning_rate=lr).minimize(cost)
# train_op = tf.train.MomentumOptimizer(learning_rate=lr, momentum = 0.9).minimize(cost)
train_op = tf.train.AdamOptimizer(learning_rate=lr).minimize(cost)


predict_op = tf.reshape(py_x, [-1, Length, Char_Numbers]) # -1表示不指定大小，自动计算
max_id_p = tf.argmax(predict_op, 2)
max_id_l = tf.argmax(tf.reshape(Y, [-1, Length, Char_Numbers]), 2)
correct_pred = tf.equal(max_id_p, max_id_l)
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
tf.summary.scalar("accuracy", accuracy)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter("./logs/nn_logs", sess.graph)  # for 1.0
    merged = tf.summary.merge_all()

    for i in range(5000):
        batch_x, batch_y = get_batch(64)

        _,loss = sess.run([train_op,cost], feed_dict={X: batch_x, Y:batch_y,p_keep_conv: 0.8, p_keep_hidden: 0.5})
        print(i,loss)

        if i % 100 == 0:
            batch_x_test, batch_y_test = get_batch(100)
            summary,acc = sess.run([merged,accuracy], feed_dict={X: batch_x_test, Y: batch_y_test, p_keep_conv: 0.8, p_keep_hidden: 0.5})
            writer.add_summary(summary, i)  # Write summary
            print(i, acc)
            if acc>0.9:
                break
    writer.close()



