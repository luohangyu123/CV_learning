import cv2
import numpy as np

# 读取视频文件
cap = cv2.VideoCapture("../img/DOG.wmv")
# # 获取视频的属性
# retval = cap.get(5)
# print(retval)
# # 判断是否读取成功
# while(cap.isOpened()):
#     # 获取每一帧图像
#     ret, frame = cap.read()
#     # 是否获取帧成功
#     if ret == True:
#         cv2.imshow("frame", frame)
#     if cv2.waitKey(25) & 0xFF == ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
# 2. 获取图像的属性（宽和高，）,并将其转换为整数
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# 3. 创建保存视频的对象，设置编码格式，帧率，图像的宽高等
out = cv2.VideoWriter('out.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
while (True):
    # 4.获取视频中的每一帧图像
    ret, frame = cap.read()
    if ret == True:
        # 5.将每一帧图像写入到输出文件中
        out.write(frame)
    else:
        break

    # 6.释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
