import cv2
import sys
import string

cap=cv2.VideoCapture(0)
i=0
while(1):
    ret ,frame = cap.read()
    k=cv2.waitKey(2)
    if k != -1:
        print('keyboard input:'+ str(k))
    if k == ord('q'):            #按下q退出窗口
        break
    elif k == ord('s'):          #按下s保存图片
        cv2.imwrite('./'+str(i)+'.jpg',frame)
        i+=1
    cv2.imshow("capture", frame)
cap.release()
