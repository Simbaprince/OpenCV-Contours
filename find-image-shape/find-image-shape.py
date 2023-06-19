import cv2
import imutils
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

# detect black shape using HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([0,0,0])
upper = np.array([180,255,30])
mask = cv2.inRange(hsv, lower, upper)

# detect black shape using BGR
#
# lower = np.array([0,0,0])
# upper = np.array([15,15,15])
# mask = cv2.inRange(hsv, lower, upper)


# show mask
cv2.imshow('mask', mask)

# contour
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# print amount of number of black objects
print('i found {} black object'.format(len(cnts)))

for c in cnts:
    cv2.drawContours(image, [c], -1, (0,255,0), 2)
    cv2.imshow('black shape', image)
    cv2.waitKey(0)

