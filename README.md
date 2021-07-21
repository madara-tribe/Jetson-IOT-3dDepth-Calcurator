# Jetson-Realtime-3dDepth-Calcurator

Use onnx yolov4-tiny to calcurate 3d depth distance with camera on jetson.
It estimate distances as car driving camera depth estimate system or rifle scope supporter.

It estimate for objects like truch, car and person
Its situation is limited on ```(1216, 1936)``` screen. this depth calcurator can be used on the limited environment. 


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

<img src="https://user-images.githubusercontent.com/48679574/126508415-888986c2-c81d-4e29-9432-bf71f84304c0.png" width="600px"><img src="https://user-images.githubusercontent.com/48679574/126508452-2b94da56-ee12-4c20-91f8-36a2b5f3b840.png" width="600px">


## sample driving video and gif
<b>Video</b>

https://user-images.githubusercontent.com/48679574/126367838-ccab8a22-9741-4ffc-a8dd-fa60a179f54b.mp4


<b>GIF</b>

![sample_driving](https://user-images.githubusercontent.com/48679574/126509431-ed5e0c31-c959-4771-a91d-b49567a0cd0d.gif)

# References
- [yolov2-and-distance-estimation](https://github.com/muhammadshiraz/Real-time-object-detection-using-yolov2-and-distance-estimation)
