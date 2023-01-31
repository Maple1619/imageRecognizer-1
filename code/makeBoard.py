import numpy as np
import cv2

board = []
for i in range(8):
    boardTemp = []
    for j in range(8):
        boardTemp.append(0)
    board.append(boardTemp)

halfWidth = int(len(board) / 2) - 1
halfHeight = int(len(board[0]) / 2) - 1

board[halfWidth][halfHeight] = 1
board[halfWidth][halfHeight+1] = 2
board[halfWidth+1][halfHeight] = 2
board[halfWidth+1][halfHeight+1] = 1

''' 
방해물을 어떻게 인식할 것 인가
'''

image = cv2.imread('../images/cropped/cropImg_1.jpg')
height, width, channel = image.shape

cv2.imshow('image', image)
cv2.waitKey(0)
cellWidth = int(width / 8)
cellHeight = int(height / 8)

xIndex = 0
yIndex = 0
for y in range(int(cellHeight / 2), height, cellHeight):
    for x in range(int(cellWidth / 2), width, cellWidth):
        b = image.item(y, x, 0)
        g = image.item(y, x, 1)
        r = image.item(y, x, 2)

        gray = (int(b) + int(g) + int(r)) / 3.0

        print("x is : ", x)
        print("y is : ", y)
        print("gray: ", gray)
        # 장애물의 max값 48정, 방해물이 아닌 칸 130 넘음.
        if(gray <= 60):
            board[xIndex][yIndex] = -1
        yIndex += 1  
    xIndex += 1
    yIndex = 0

print(np.array(board))
        
