import cv2
import numpy as np

def get_ball(image):
    radius = 20
    color = (255, 0, 0)
    thickness = -1
    center_coordinates = (50, 50)
    new_image = cv2.circle(image, center_coordinates, radius, color, thickness)
    return new_image

def change_colour(image):
    (rows, cols, height) = np.shape(image)
    #print(rows)
    #print(cols)
    red_img = np.full((rows, cols, 3), (0, 0, 255), np.uint8)
    new_image = cv2.add(image, red_img)
    return new_image

def colourize_image(image):
    hsvim = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #lower = np.array([0, 10, 60], dtype="uint8")
    #upper = np.array([20, 150, 255], dtype="uint8")
    sensitivity = 70

    lower = np.array([0, 0, 255 - sensitivity])
    upper = np.array([360, sensitivity, 255])
    skinRegionHSV = cv2.inRange(hsvim, lower, upper)
    blurred = cv2.blur(skinRegionHSV, (2, 2))
    ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)
    #return thresh

    #print(thresh)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    try:
        contours = max(contours, key=lambda x: cv2.contourArea(x))
        #print(contours)
        cv2.drawContours(image, [contours], -1, (255, 255, 0), 2)
        #cnt = contours[0]
        hull = cv2.convexHull(contours, returnPoints=False)
        #cv2.drawContours(image, hull, -1, (0, 255, 255), 2)
        #print(hull)
        defects = cv2.convexityDefects(contours, hull)
        #print(defects)
        if defects is not None:
            cnt = 0
        for i in range(defects.shape[0]):  # calculate the angle
            s, e, f, d = defects[i][0]
            start = tuple(contours[s][0])
            end = tuple(contours[e][0])
            far = tuple(contours[f][0])
            a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
            if angle <= np.pi / 2:  # angle less than 90 degree, treat as fingers
                cnt += 1
                cv2.circle(image, far, 4, [0, 0, 255], -1)
            print(cnt)
        if cnt > 0:
            cnt = cnt + 1
        cv2.putText(image, str(cnt), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    except:
        pass
    return image

    #cv2.imshow("thresh", thresh)
    #print('test')