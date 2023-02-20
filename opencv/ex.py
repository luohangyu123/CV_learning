import numpy as np
import cv2
# 以图的形式读取图像
from matplotlib import pyplot as plt

img = cv2.imread('../img/1.jpg', 0)

# opencv中显示
# cv2.imshow('image', img)
# cv2.waitKey(0)
# matplotlib中展示
# plt.imshow(img[:, :, ::-1])
plt.imshow(img, cmap=plt.cm.gray)
plt.show()

# cv2.imwrite('../img/1.png', img)

# img = np.zeros((512, 512, 3), np.uint8)
# cv2.line(img, (0, 0), (200, 200), (255, 0, 0), 2)
# cv2.circle(img, (200, 200), 100, (0, 255, 0), 2)
# cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 255), 2)
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
#
# cv2.imshow('image', img)
# cv2.waitKey(0)