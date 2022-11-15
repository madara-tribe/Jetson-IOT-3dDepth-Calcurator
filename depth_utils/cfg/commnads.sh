# !/bin/sh
# pytorch to onnx
python3 demo_pytorch2onnx.py ../weights/yolov4.pth dog.jpg 1 80 416 416

# Darknet to onnx
python3 demo_darknet2onnx.py yolov4.cfg ../weights/yolov4.weights dog.jpg 1


