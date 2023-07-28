import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# 步骤1：准备数据集并导入必要的库和数据（假设使用MNIST数据集）
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 步骤3：预处理数据
train_images, test_images = train_images / 255.0, test_images / 255.0
train_labels = tf.one_hot(train_labels, 10)
test_labels = tf.one_hot(test_labels, 10)

# 步骤4：构建神经网络模型
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 步骤5：编译模型
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 步骤6：训练模型
model.fit(train_images, train_labels, epochs=10, batch_size=32)

# 步骤7：保存模型
model.save('digit_recognition_model.keras')


predictions = model.predict([test_images[0]])

# 预测结果是一个包含概率的数组，对应于每个数字的概率
# 可以通过取最大概率的索引来获取预测的数字
predicted_label = np.argmax(predictions)

print("预测结果为：", predicted_label)