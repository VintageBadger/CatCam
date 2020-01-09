from imutils.video import VideoStream
import argparse
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    # read() Grabs, decodes and returns the next video frame
    # if camera disconnected or no more frames in video, returns false and empty image
    ret, frame = cap.read()

    # Our operations on the frame come here
    # cvtColor(src, dst, code = color space conversion, dstCn = num of channels in dst) 
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cie = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ) #oranges turn blue
    # YCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb) #lots of yellows and pinks
    # No color transformations are needed, but they are fun :)

    # Display the resulting frame
    cv2.imshow('CatCam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
