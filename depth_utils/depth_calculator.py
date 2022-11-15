import sys, math
import numpy as np
import cv2

def perspective_dist_calculator(startX, startY, endX, endY, img_w, img_h, cls_name, box):
    # img_w == 1216
    
    x_1, y_1, x_2, y_2 = startX, startY, endX, endY  # top left of the triangle
    x0, y0 = img_w / 2, img_h # bottom of the triangle
    
    # find the angle between bottom and right point
    angle_right = 90 + math.degrees(math.atan2(x0 - x_2, y0 - y_2))
    # find the angle between bottom and left point
    angle_left = 90 - math.degrees(math.atan2(x0 - x_1, y0 - y_1))
    angle_ratio = (angle_right + angle_left)**2 / 1000
    
    #### sub ratio
    sub_ratio = (img_w - endY)**2 / 1000
    pos_adjust_param = 0.0026
    
    return np.round(sub_ratio * angle_ratio * pos_adjust_param, decimals=2)
