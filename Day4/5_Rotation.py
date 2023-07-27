import cv2

img = cv2.imread('dog.bmp')
cp = (img.shape[1] / 2, img.shape[0]/2)
rot = cv2.getRotationMatrix2D(cp, 20, 0.5)
dst = cv2.warpAffine(img, rot, (0, 0))
# 회전을 적용시키고 싶으면 warpAffine에 넣어야 한다.

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()