import cv2
import numpy as np

def get_ball(image):
    radius = 20
    color = (255, 0, 0)
    thickness = -1
    center_coordinates = (50, 50)
    new_image = cv2.circle(image, center_coordinates, radius, color, thickness)
    return new_image

def colourize_image(image):
    hsvim = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 48, 80], dtype="uint8")
    upper = np.array([20, 255, 255], dtype="uint8")
    skinRegionHSV = cv2.inRange(hsvim, lower, upper)
    blurred = cv2.blur(skinRegionHSV, (2, 2))
    ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)
    return thresh
    #cv2.imshow("thresh", thresh)
    #print('test')