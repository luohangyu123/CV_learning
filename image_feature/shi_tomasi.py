import numpy as np
import cv2
import matplotlib.pyplot as plt

# 1 读取图像
img = cv2.imread('../img/tv.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 2 角点检测
corners = cv2.goodFeaturesToTrack(gray, 1000, 0.01, 10)
# 3 绘制角点
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (int(x), int(y)), 2, (0, 0, 255), -1)
# 4 图像展示
plt.figure(figsize=(10, 8), dpi=100)
plt.imshow(img[:, :, ::-1]), plt.title('shi-tomasi角点检测')
plt.xticks([]), plt.yticks([])
plt.show()
