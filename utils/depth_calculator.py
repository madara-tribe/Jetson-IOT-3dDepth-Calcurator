import sys, math
import numpy as np
import cv2

def perspective_dist_calculator(startX, startY, endX, endY, img_w, img_h, cls_name, box):
    def cal_box_ratio(box, div=5):
        box_ratio = 1- (box[3]-box[1])*2 if (box[3]-box[1]) > 0.1 else 1 - (box[3]-box[1])**div
        return box_ratio * 10
    
    x_1, y_1, x_2, y_2 = startX, startY, endX, endY
    x0, y0 = img_w / 2, 0 # bottom of the triangle

    # find the angle between bottom and right point
    angle_right = 90 + math.degrees(math.atan2(x0 - x_2, y0 - y_2))
    # find the angle between bottom and left point
    angle_left = 90 - math.degrees(math.atan2(x0 - x_1, y0 - y_1))
    angle_ratio = angle_right + angle_left
    
    #### sub ratio
    sub_ratio = ((img_h - y_2)/1000)**3
    box_ratio = cal_box_ratio(box, div=10)
    #print('angle sub box', angle_ratio, sub_ratio, box_ratio)
    if cls_name=='person':
        adjust_param = 0.005
    elif cls_name=='car':
        adjust_param = 0.005
    else:
        adjust_param = 0.005
    total_ratio = angle_ratio * sub_ratio * box_ratio
    return np.round(abs(adjust_param * total_ratio), decimals=2)
