import cv2
import matplotlib.pyplot as plt

# 1.以灰度图的形式读取图片
img = cv2.imread("../img/5.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(cv2.__file__)
# 2.实例化OpenCV人脸和眼睛识别的分类器
# 这里需要使用绝对路径
face_cas = cv2.CascadeClassifier("D:/programmingSW/anaconda3/envs/pyhton3_1/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
face_cas.load('D:/programmingSW/anaconda3/envs/pyhton3_1/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

eyes_cas = cv2.CascadeClassifier("D:/programmingSW/anaconda3/envs/pyhton3_1/Lib/site-packages/cv2/data/haarcascade_eye.xml")
eyes_cas.load("D:/programmingSW/anaconda3/envs/pyhton3_1/Lib/site-packages/cv2/data/haarcascade_eye.xml")

# 3.调用识别人脸
faceRects = face_cas.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
for faceRect in faceRects:
    x, y, w, h = faceRect
    # 框出人脸
    cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 3)
    # 4.在识别出的人脸中进行眼睛的检测
    roi_color = img[y:y + h, x:x + w]
    roi_gray = gray[y:y + h, x:x + w]
    eyes = eyes_cas.detectMultiScale(roi_gray)

    num = 0
    for (ex, ey, ew, eh) in eyes:
        num += 1
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
# 5. 检测结果的绘制
plt.figure(figsize=(8, 6), dpi=100)
plt.imshow(img[:, :, ::-1]), plt.title('detect_result')
plt.xticks([]), plt.yticks([])
plt.show()
