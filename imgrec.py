import cv2
import numpy as np
import os
import re
dirPath = './images'
p = re.compile('cap\d.png')
imgPaths = []
imgNames=[]
for f in os.listdir(dirPath):
    if p.match(f):
        imgPaths.append(os.path.join(dirPath,f))
        imgNames.append(f.rstrip('.png'))
for imgpath in imgPaths:
    print(imgpath)
    image = cv2.imread(imgpath, cv2.IMREAD_COLOR)
    original = image.copy()
    cv2.imshow('original',original)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray',gray)
    ksize=(3,3)
    blur = cv2.GaussianBlur(gray, ksize=ksize, sigmaX=0)
    # cv2.imshow('blurIMG', blur)
    retINV, threshINV = cv2.threshold(blur, 0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    s = f'{ksize}_THRINV'
    # cv2.imshow(s, threshINV)
    vertikernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,50))
    openedINV = cv2.morphologyEx(threshINV, cv2.MORPH_OPEN, vertikernel)
    # cv2.imshow('openingVerti', openedINV)
    horikernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50,1))
    openedINV = cv2.morphologyEx(openedINV, cv2.MORPH_OPEN, horikernel)
    # cv2.imshow('openingHori', openedINV)
    mode=cv2.RETR_EXTERNAL;method=cv2.CHAIN_APPROX_SIMPLE
    contours, hierarchy = cv2.findContours(openedINV.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    mask = np.zeros(image.shape, dtype=np.uint8)
    for contour in contours:
        area = cv2.contourArea(contour)
        '''
        권장 사이즈를 측정할 필요 있다. 메이플 스토리의 창모드의 pixel 크기는 유동적으로 조정할 수 있으니, 
        여기서 적당한 보드판의 크기를 유추하여 contour를 검출하면 된다.
        '''
        if 100000 < area :
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x,y),(x+w, y+h), (0,255,0), 3)
            # cv2.drawContours(image, [contour], 0, (0,255,0), 3)
            cv2.rectangle(mask,(x,y),(x+w, y+h), (255,255,255), -1)
            print(area)

    mask = cv2.bitwise_and(mask, original)
    # contours_image = cv2.drawContours(original.copy(), contours, -1, (0,255,0), 3)
    name = f'blogIMG/CONTOUR_{method}_{mode}.jpg'
    # cv2.imshow(name,contours_image)
    cv2.imshow(name,image)
    cv2.imshow('mask',mask)

    cv2.waitKey()