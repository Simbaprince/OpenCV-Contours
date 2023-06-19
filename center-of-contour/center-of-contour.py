import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args['image'])

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blurred image
blur = cv2.GaussianBlur(gray, (5,5), 0)

# treshold 
tresh = cv2.threshold(blur, 80, 255, cv2.THRESH_BINARY)[1]



# find contours in the thresholded image
cnts = cv2.findContours(tresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:

    # compute the center of the contour
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(image, (cX, cY), 5, (255, 255, 255), -1)
    
    # draw outlines
    cv2.drawContours(image, [c], -1, (0,255,0), 2)

    # draw text
    cv2.putText(image, 'center', (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

    # show image
    cv2.imshow('img', image)
    cv2.waitKey(0)
