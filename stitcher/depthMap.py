# import the necessary packages
import stitcher
import argparse
import imutils
import cv2
import numpy as np
import time

imageA = cv2.imread("../stitching_img2/image002.png") # top left
imageB = cv2.imread("../stitching_img2/image003.png") # top Right

stitch = stitcher.Stitcher()

ratio=0.75
reprojThresh=4.0
(kpsA, featuresA) = stitch.detectAndDescribe(imageA)
(kpsB, featuresB) = stitch.detectAndDescribe(imageB)
# match features between the two images
M1 = stitch.matchKeypoints(kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh)
(matches, H1, status) = M1
M2 = stitch.matchKeypoints(kpsB, kpsA, featuresB, featuresA, ratio, reprojThresh)
(matches, H2, status) = M2

print "\n1:"
(result1, vis1) = stitch.stitch([imageA, imageB], showMatches=True)
print "\n2:"
(result2, vis1) = stitch.stitch([imageB, imageA], showMatches=True)

(kpsA, featuresA) = stitch.detectAndDescribe(result1)
(kpsB, featuresB) = stitch.detectAndDescribe(result2 )
# match features between the two images
M1 = stitch.matchKeypoints(kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh)
(matches, H1, status) = M1
M2 = stitch.matchKeypoints(kpsB, kpsA, featuresB, featuresA, ratio, reprojThresh)
(matches, H2, status) = M2

print H1
print H2
print np.dot(H1,H2)

# show the images
cv2.imshow("Result 1", result1)
cv2.imshow("Result 2", result2)
cv2.waitKey(0)
