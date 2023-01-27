import cv2
import numpy as np

def perspective_transform(image, corners):
    def order_corner_points(corners):
        # Separate corners into individual points
        # Index 0 - top-right
        #       1 - top-left
        #       2 - bottom-left
        #       3 - bottom-right
        corners = [(corner[0][0], corner[0][1]) for corner in corners]
        top_r, top_l, bottom_l, bottom_r = corners[0], corners[1], corners[2], corners[3]
        return (top_l, top_r, bottom_r, bottom_l)

    # Order points in clockwise order
    ordered_corners = order_corner_points(corners)
    top_l, top_r, bottom_r, bottom_l = ordered_corners

    # Determine width of new image which is the max distance between 
    # (bottom right and bottom left) or (top right and top left) x-coordinates
    width_A = np.sqrt(((bottom_r[0] - bottom_l[0]) ** 2) + ((bottom_r[1] - bottom_l[1]) ** 2))
    width_B = np.sqrt(((top_r[0] - top_l[0]) ** 2) + ((top_r[1] - top_l[1]) ** 2))
    width = max(int(width_A), int(width_B))

    # Determine height of new image which is the max distance between 
    # (top right and bottom right) or (top left and bottom left) y-coordinates
    height_A = np.sqrt(((top_r[0] - bottom_r[0]) ** 2) + ((top_r[1] - bottom_r[1]) ** 2))
    height_B = np.sqrt(((top_l[0] - bottom_l[0]) ** 2) + ((top_l[1] - bottom_l[1]) ** 2))
    height = max(int(height_A), int(height_B))

    # Construct new points to obtain top-down view of image in 
    # top_r, top_l, bottom_l, bottom_r order
    dimensions = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], 
                    [0, height - 1]], dtype = "float32")

    # Convert to Numpy format
    ordered_corners = np.array(ordered_corners, dtype="float32")

    # Find perspective transform matrix
    matrix = cv2.getPerspectiveTransform(ordered_corners, dimensions)

    # Return the transformed image
    return cv2.warpPerspective(image, matrix, (width, height))

# image = cv2.imread('images/similarcap.png')
image = cv2.imread('images/trashcap.png')
original = image.copy()
blur = cv2.bilateralFilter(image,-1,1,5)
gray1 = cv2.cvtColor(blur, cv2.COLOR_BGRA2GRAY)
gray2 = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(blur, cv2.COLOR_BGR2HLS)
tmp1 = cv2.cvtColor(gray3, cv2.COLOR_BGR2GRAY)
light = cv2.cvtColor(blur, cv2.COLOR_BGR2LAB)

cv2.imshow('gray1', gray1)
cv2.imshow('gray2', gray2)
cv2.imshow('gray3', gray3)
cv2.imshow('tmp1', tmp1)
cv2.imshow('light', light)
cv2.waitKey()

# threshimg = cv2.threshold(gray1,112,255, cv2.THRESH_BINARY_INV)[1]
# cv2.imshow('thimg1',threshimg)
# threshimg = cv2.threshold(gray2,112,255, cv2.THRESH_BINARY_INV)[1]
# cv2.imshow('thimg2',threshimg)
threshimg = cv2.threshold(gray3,112,255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow('thimg3',threshimg)
# threshimg = cv2.threshold(tmp1,112,255, cv2.THRESH_BINARY_INV)[1]
# cv2.imshow('thimg4',threshimg)

# threshimg = cv2.threshold(light,112,255, cv2.THRESH_BINARY_INV)[1]
# cv2.imshow('thimg5',threshimg)
cv2.waitKey()
# for thresh in range(100,130):
#     name=f'thresh{thresh}'
#     threshimg = cv2.threshold(gray,thresh,255, cv2.THRESH_BINARY_INV)[1]
#     cv2.imshow(name, threshimg)
#     cv2.waitKey()


# cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# mask = np.zeros(image.shape, dtype=np.uint8)
# for c in cnts:
#     area = cv2.contourArea(c)
#     peri = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.015 * peri, True)

#     if area > 150000 and len(approx) == 4:
#         cv2.drawContours(image,[c], 0, (36,255,12), 3)
#         cv2.drawContours(mask,[c], 0, (255,255,255), -1)
#         transformed = perspective_transform(original, approx)

# mask = cv2.bitwise_and(mask, original)

# cv2.imshow('thresh', thresh)
# cv2.imshow('image', image)
# cv2.imshow('mask', mask)
# cv2.imshow('transformed', transformed)
cv2.waitKey()