# Jetson-IOT-3dDepth-Calcurator

Use onnx yolov4-tiny to calcurate 3d depth distance with camera on jetson or Qt6.
It estimate distances as car driving camera depth estimate system.

It estimate for objects like truch, car and person.

Use oriinal formula to calcurate 3d depth distance. 
So, capture image size are limited ```(1216, 1936)``` screen. this depth calcurator can be used in the limited environment. 


Sample driving movie
- [sample driving movie](https://drive.google.com/file/d/1czoTCb-Qud-LXYEMzN28TbWLxWAqNUh-/view?usp=sharing)


# inference command 

## PyQt6 
```zsh
$ python3 main.py --qtapp
```

## inference for Single image

## camera inference
```zsh
$ python3 main.py --camera
```

# current result

<img src="https://user-images.githubusercontent.com/48679574/126508415-888986c2-c81d-4e29-9432-bf71f84304c0.png" width="600px"><img src="https://user-images.githubusercontent.com/48679574/126508452-2b94da56-ee12-4c20-91f8-36a2b5f3b840.png" width="600px">


## sample driving video and gif
<b>Video</b>

https://user-images.githubusercontent.com/48679574/126510617-03ef8cac-eed5-414c-aad2-62cc69457dd7.mp4


<b>GIF</b>

![sample_driving](https://user-images.githubusercontent.com/48679574/126509431-ed5e0c31-c959-4771-a91d-b49567a0cd0d.gif)

# References
- [yolov2-and-distance-estimation](https://github.com/muhammadshiraz/Real-time-object-detection-using-yolov2-and-distance-estimation)
