import cv2

def get_ball(image):
    radius = 20
    color = (255, 0, 0)
    thickness = -1
    center_coordinates = (50, 50)
    new_image = cv2.circle(image, center_coordinates, radius, color, thickness)
    return new_image
