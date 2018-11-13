import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

train_images = mnist.train.images
train_labels = mnist.train.labels
test_images = mnist.test.images
test_labels = mnist.test.labels

print("train_images_shape:", train_images.shape)
print("train_labels_shape:", train_labels.shape)
print("test_images_shape:", test_images.shape)
print("test_labels_shape:", test_labels.shape)
print("train_images:\n", train_images[0])
print("train_images_length:",len(train_images[0]))
print("train_labels:", train_labels[0])
