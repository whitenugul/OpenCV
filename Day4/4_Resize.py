import cv2

img = cv2.imread('dog.bmp')
dst1 = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_CUBIC)

cv2.imshow('img', img)
cv2.imshow('dst1', dst1[400:800, 200:600])
cv2.imshow('dst2', dst2[400:800, 200:600])
cv2.waitKey()

# 확대를 시켜서 비교를 해보니 INTER_NEAREST가 픽셀이 더 잘 보인다.
# 화질이 더 안 좋은걸 알 수 있다.
