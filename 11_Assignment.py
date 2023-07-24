import cv2
import numpy as np
cap1 = cv2.VideoCapture('./bird.mp4')
cap2 = cv2.VideoCapture('./duck.mp4')

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
print(frame_cnt1)
print(frame_cnt1)
fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)
print(fps1)
print(fps2)
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('w', w)
print('h', h)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('mix.avi', fourcc, fps1, (w, h))

fade_duration = 2

for i in range(frame_cnt1):
    ret1, frame1 = cap1.read()
    if i < (frame_cnt1 - int(fps1) * fade_duration):
        cv2.imshow('output', frame1)
    else:
        alpha = 1.0 - (i - (frame_cnt1 - int(fps1) * fade_duration)) / (int(fps1) * fade_duration)
        overlay = frame1.copy()
        cv2.rectangle(overlay, (int(w * alpha), 0), (w, h), (0, 0, 0), -1)
        cv2.addWeighted(overlay, alpha, frame1, 1 - alpha, 0, frame1)
        cv2.imshow('output', frame1)

    out.write(frame1)
    if cv2.waitKey(10) == 27:
        break
for i in range(frame_cnt2):
    ret2, frame2 = cap2.read()
    cv2.imshow('output', frame2)

    if i < int(fps2) * fade_duration:
        alpha = i / (int(fps2) * fade_duration)
        overlay = frame2.copy()
        cv2.rectangle(overlay, (0, 0), (int(w * alpha), h), (0, 0, 0), -1)
        cv2.addWeighted(overlay, alpha, frame2, 1 - alpha, 0, frame2)

    out.write(frame2)
    if cv2.waitKey(10) == 27:
        break


cap1.release()
cap2.release()
out.release()