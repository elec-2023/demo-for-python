import tensorflow as tf
import numpy as np
from PIL import Image

# 步骤1：导入必要的库和模型文件
# 假设之前保存的模型文件名为'digit_recognition_model.h5'
model = tf.keras.models.load_model('digit_recognition_model.keras')

# 步骤2：使用模型进行预测
# 假设有新的手写数字图像数据，你需要将其预处理成与训练数据相同的格式
# new_data = np.random.rand(1, 28, 28)  # 这里假设有一个随机生成的28x28图像作为示例
image_path = 'img.png'
image = Image.open(image_path).convert('L')  # 转为灰度图像
image = image.resize((28, 28))  # 调整大小为28x28像素
image_array = np.array([np.array(image) / 255.0])  # 将像素值缩放到0到1之间

# 使用模型进行预测
predictions = model.predict(image_array)

# 预测结果是一个包含概率的数组，对应于每个数字的概率
# 可以通过取最大概率的索引来获取预测的数字
predicted_label = np.argmax(predictions)

print("预测结果为：", predicted_label)
