# Opencv Contour

## What are contours?

Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition.

- For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
- Since OpenCV 3.2, findContours() no longer modifies the source image but returns a modified image as the first of three return parameters.
- In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.


## Project
a collection of several projects that involve contour techniques in opencv

- [finding center of contour](center-of-contour/)
- [finding image shapes](find-image-shape/)
- [finding extreme points in contour](find-extreme-points/)
- [sorting contour](sorting-contour/)