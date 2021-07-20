import sys
import onnx
import os
import argparse
import numpy as np
import cv2
import onnxruntime
import time
import math
from utils.utils import nms_cpu, load_class_names, post_processing
from utils.depth_calculator import perspective_dist_calculator



def bbox_xy(box, W, H, color=False):
    x1 = int(box[0] * W)
    y1 = int(box[1] * H)
    x2 = int(box[2] * W)
    y2 = int(box[3] * H)

    if color:
        rgb = color
    else:
        rgb = (255, 0, 0)
    return x1, y1, x2, y2, rgb
    
def plot_boxes_cv2(img, boxes, savename=None, class_names=None, color=None):
    img = np.copy(img)
    colors = np.array([[1, 0, 1], [0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0], [1, 0, 0]], dtype=np.float32)

    def get_color(c, x, max_val):
        ratio = float(x) / max_val * 5
        i = int(math.floor(ratio))
        j = int(math.ceil(ratio))
        ratio = ratio - i
        r = (1 - ratio) * colors[i][c] + ratio * colors[j][c]
        return int(r * 255)

    height, width = img.shape[:2]
    for i in range(len(boxes)):
        box = boxes[i]
        x1, y1, x2, y2, rgb = bbox_xy(box, W=width, H=height, color=color)
        
        if len(box) >= 7 and class_names:
            cls_conf = box[5]
            cls_id = box[6]
            print('%s: %f' % (class_names[cls_id], cls_conf))
            classes = len(class_names)
            offset = cls_id * 123457 % classes
            red = get_color(2, offset, classes)
            green = get_color(1, offset, classes)
            blue = get_color(0, offset, classes)
            if color is None:
                rgb = (red, green, blue)
            if not str(class_names[cls_id]) in ['car', 'person', 'truck']:
                continue
            depth_dist = perspective_dist_calculator(x1, y1, x2, y2, height, width, class_names[cls_id], box)
            print('cal depth distance is ', depth_dist)
            #img = cv2.putText(img, class_names[cls_id], (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.2, rgb, 1)
            img = cv2.putText(img, str(depth_dist)+' M', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, rgb, 3)
        img = cv2.rectangle(img, (x1, y1), (x2, y2), rgb, 1)
    if savename:
        print("save plot results to %s" % savename)
        cv2.imwrite(savename, img)
    return img


    
def movie_main(onnx_path_demo, image_src):

    session = onnxruntime.InferenceSession(onnx_path_demo)
    # session = onnx.load(onnx_path)
    print("The model expects input shape: ", session.get_inputs()[0].shape)
    detected_img = detect(session, image_src, movie=True)
    return detected_img


def image_main(onnx_path_demo, image_path):

    session = onnxruntime.InferenceSession(onnx_path_demo)
    # session = onnx.load(onnx_path)
    print("The model expects input shape: ", session.get_inputs()[0].shape)
    image_src = cv2.imread(image_path)
    detected_img = detect(session, image_src, movie=False)
    return detected_img


def detect(session, image_src, movie=True):
    IN_IMAGE_H = session.get_inputs()[0].shape[2]
    IN_IMAGE_W = session.get_inputs()[0].shape[3]

    # Input
    resized = cv2.resize(image_src, (IN_IMAGE_W, IN_IMAGE_H), interpolation=cv2.INTER_LINEAR)
    img_in = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    img_in = np.transpose(img_in, (2, 0, 1)).astype(np.float32)
    img_in = np.expand_dims(img_in, axis=0)
    img_in /= 255.0
    print("Shape of the network input: ", img_in.shape)

    # Compute
    input_name = session.get_inputs()[0].name

    outputs = session.run(None, {input_name: img_in})

    boxes = post_processing(img_in, 0.4, 0.6, outputs)

    num_classes = 80
    if num_classes == 20:
        namesfile = 'src/voc.names'
    elif num_classes == 80:
        namesfile = 'src/coco.names'
    else:
        namesfile = 'src/x.names'

    class_names = load_class_names(namesfile)
    if movie:
        img = plot_boxes_cv2(image_src, boxes[0], savename=None, class_names=class_names)
    else:
        img = plot_boxes_cv2(image_src, boxes[0], savename='pred_img.png', class_names=class_names)
    return img

if __name__ == '__main__':
    print("Converting to onnx and running demo ...")
    onnx_file_path = sys.argv[1]
    image_path = sys.argv[2]
    image_main(onnx_file_path, image_path)
  
    print('Please run this way:\n')
    print('python demo_onnx.py <onnxweightFile> <imageFile>')
