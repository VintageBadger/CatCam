import numpy as np
import cv2
from PIL import Image

img1 = cv2.imread('Floofers.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('KingFloof.jpg', cv2.IMREAD_COLOR)

#blank = Image.new('RGB', (604, 806), color = 'white')
#blank.save('white.jpg')
white = cv2.imread('white.jpg', cv2.IMREAD_COLOR)


while(True):
    #resize the super large Floofers image
    #original details are Size: 3.21MB Resolution: 4032x3024
    #scaled Resolution: 806x604
    scale_percent = 20 # percent of original size
    width1 = int(img1.shape[1] * scale_percent / 100)
    width2 = int(img2.shape[1] * scale_percent / 100)
    height1 = int(img1.shape[0] * scale_percent / 100)
    height2 = int(img2.shape[0] * scale_percent / 100)
    dim1 = (width1, height1)
    dim2 = (width2, height2)
    # resize image
    resized1 = cv2.resize(img1, dim1, interpolation = cv2.INTER_AREA)
    resized2 = cv2.resize(img2, dim2, interpolation = cv2.INTER_AREA)

    #get sub-image of img1(Floofers)
    roi_img1 = resized1[150:500, 180:450]

    #paste floofers onto white image in bottom left corner
    #image[height_range, width_range]
    white[456:806, 0:270] = roi_img1

    # Display the resulting image
    cv2.imshow('Floofers', resized1)
    cv2.imshow('roi', roi_img1)
    cv2.imshow('KingFloof', resized2)
    cv2.imshow('White', white)

    #add images together
    weighted = cv2.addWeighted(white, 0.7, resized2, 0.3, 0)
    cv2.imshow('Weighted', weighted)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
