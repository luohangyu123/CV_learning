import cv2
import numpy as np

# 1.读取视频文件
cap = cv2.VideoCapture("../img/DOG.wmv")
# cap = cv2.VideoCapture("./trace.mp4")
# 2.指定追踪目标 （行，高，列，宽）
ret, frame = cap.read()
# r, h, c, w = 115, 340, 1100, 200
r, h, c, w = 197, 140, 0, 200
win = [c, r, w, h]
roi = frame[r:r + h, c:c + w]

# 3.计算直方图
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# 4.目标追踪
term = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while (True):
    ret, frame = cap.read()
    # 计算直方图的反省投影
    if ret == True:
        hst = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hst], [0], roi_hist, [0, 180], 1)
        ret, win = cv2.meanShift(dst, win, term)

        x, y, w, h = win
        img2 = cv2.rectangle(frame, (x, y), (x+w, y+h), 255, 2)
        # ret, win = cv2.CamShift(dst, win, term)
        #
        # # 绘制追踪结果
        # pts = cv2.boxPoints(ret)
        # pts = np.int0(pts)
        # img2 = cv2.polylines(frame, [pts], True, 255, 2)

        cv2.imshow("frame", img2)

        if cv2.waitKey(60) & ord("q") == 0xFF:
            break
    else:
        break
# 5.释放资源
cap.release()

cv2.destroyAllWindows()
