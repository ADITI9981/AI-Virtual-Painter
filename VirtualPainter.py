import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

folderPath = "page"
myList = os.listdir(folderPath)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))
header = overlayList[1]
drawcolor = (255,0,255)
brushThickness = 15
eraserThickness = 100
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = htm.handDetector(detectionCon=0.85)
xp, yp =0, 0
imgCanvas = np.zeros((720,1200,3),np.uint8)


while True:
    # 1. Import Image
    success, img = cap.read()
    img = cv2.flip(img,1)

    # 2.Find Hand Landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)

    if len(lmList) != 0:
        #print(lmList)

        # tip of index and middle fingers
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]


        # 3. Check Which fingers are up
        fingers = detector.fingerup()
        #print(fingers)

        # 4. If Selection mode - Two finger are up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("selection mode")
            if y1 < 125:
                if 250<x1<450:
                    header = overlayList[0]
                    drawcolor = (255,0,255)
                elif 550 < x1 <750:
                    header = overlayList[1]
                    drawcolor = (255,0,0)
                elif 800 <x1 <950:
                    header = overlayList[2]
                    drawcolor = (0,255,0)
                elif 1050 < x1 < 1200:
                    header = overlayList[3]
                    drawcolor = (0,0,0)
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawcolor, cv2.FILLED)

        # 5. If Drawing Mode - Index finger is up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img,(x1,y1),15,drawcolor, cv2.FILLED)
            print("Drawing Mode")
            if xp ==0 and yp==0:
                xp,yp = x1,y1

            if drawcolor == (0,0,0):
                cv2.line(img, (xp, yp), (x1, y1), drawcolor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawcolor, eraserThickness)

            else:
                cv2.line(img, (xp,yp),(x1,y1),drawcolor,brushThickness)
                cv2.line(imgCanvas, (xp,yp),(x1,y1),drawcolor,brushThickness)

            xp,yp =x1,y1
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    imgInv = cv2.resize(imgInv, (img.shape[1], img.shape[0]))
    img = cv2.bitwise_and(img,imgInv)
    imgCanvas = cv2.resize(imgCanvas, (img.shape[1], img.shape[0]))
    img = cv2.bitwise_or(img,imgCanvas)

    # setting the header image
    header_resized = cv2.resize(header, (1280, 125))
    img[0:125, 0:1280] = header_resized
    #img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("Image",img)
    cv2.imshow("Canvas",imgCanvas)
    cv2.imshow("Inv",imgInv)

    cv2.waitKey(1)
