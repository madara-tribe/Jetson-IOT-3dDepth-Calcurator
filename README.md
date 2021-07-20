# Jetson-Realtime-3dDepth-Calcurator

Use onnx yolov4-tiny to calcurate 3d depth distance with camera on jetson.
It estimate distances as car driving camera depth estimate system or rifle scope supporter.

It estimate for objects like truch, car and person
Its situation is limited on ```(1216, 1936)``` screen. this depth calcurator can be used on the limited use. 


Sample driving movie
- [sample driving movie](https://drive.google.com/file/d/1czoTCb-Qud-LXYEMzN28TbWLxWAqNUh-/view?usp=sharing)


# inference command 

```zsh
# image inference
$ (/opt/anaconda3/bin/python3) python3 onnx_inference.py yolov4_1_3_416_416_static.onnx images/train_2007.jpg


# camera inference
$ (/opt/anaconda3/bin/python3) python3 camera_estimation.py yolov4_1_3_416_416_static.onnx

```

# current result

<img src="https://user-images.githubusercontent.com/48679574/126335148-931e66df-6fe9-4a39-9879-b0c56c2f191e.png" width="600px"><img src="hhttps://user-images.githubusercontent.com/48679574/126335157-7156a2b0-8814-4420-8eb0-ae4ac5eea78e.png" width="600px">


## sample driving video
https://user-images.githubusercontent.com/48679574/126075780-1189181a-0751-47e7-906f-69c62acdef85.mov

![sample](https://user-images.githubusercontent.com/48679574/126086372-22c6e710-f645-40a4-91f3-c9728337393c.gif)


# References
- [yolov2-and-distance-estimation](https://github.com/muhammadshiraz/Real-time-object-detection-using-yolov2-and-distance-estimation)
