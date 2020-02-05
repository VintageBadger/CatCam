from imutils.video import VideoStream
import numpy as np
import cv2
import matplotlib.pyplot as plt

try:
    cap = cv2.VideoCapture(0)
except Exception as e:
    print("Error getting videocapture" + e)
while(True):
    # Capture frame-by-frame
    # read() Grabs, decodes and returns the next video frame
    # if camera disconnected or no more frames in video, returns false and empty image
    ret, frame = cap.read()

    # Our operations on the frame come here
    # cvtColor(src, dst, code = color space conversion, dstCn = num of channels in dst)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cie = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ) #oranges turn blue
    # YCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb) #lots of yellows and pinks
    # No color transformations are needed, but they are fun :)

    # Display the resulting frame
    cv2.imshow('CatCam Original', frame)
    cv2.imshow('CatCam Gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
