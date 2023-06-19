import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args['image'])

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blur the image
blurred = cv2.GaussianBlur(gray, (5,5), 0)

# threshold the image
thresh = cv2.threshold(blurred, 45, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)


# find contour
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# grab only  the large object
c = max(cnts, key=cv2.contourArea)

# determine the most extreme points along the contour
extLeft = tuple(c[c[:, :, 0].argmin()][0]) # west
extRight = tuple(c[c[:, :, 0].argmax()][0]) # east
extTop = tuple(c[c[:, :, 1].argmin()][0]) # north
extBot = tuple(c[c[:, :, 1].argmax()][0]) # south

# draw contour
cv2.drawContours(image, [c], -1, (0,255,255), 2)

# draw circle in every extreme point
cv2.circle(image, extLeft, 8, (0,0,255), -1)
cv2.circle(image, extRight, 8, (0,0,255), -1)
cv2.circle(image, extTop, 8, (0,0,255), -1)
cv2.circle(image, extBot, 8, (0,0,255), -1)

# draw text
cv2.putText(image, 'West', (extLeft[0] - 20,extLeft[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
cv2.putText(image, 'East', (extRight[0] - 40,extRight[1] - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
cv2.putText(image, 'North', (extTop[0] - 20,extTop[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
cv2.putText(image, 'South', (extBot[0] - 70,extBot[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

# show the image
cv2.imshow('img', image)
cv2.waitKey(0)

# save the image
cv2.imwrite('output.jpg', image)
