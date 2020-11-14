import cv2
import numpy as np

def image_testing(image):
    '''put your code down here'''


    '''put your code above here'''
    cv2.imshow("image",image)
    cv2.waitKey(0)

    return image


if __name__ == "__main__":
    image = cv2.imread("images/HandLines.jpg")
    image_testing(image)
