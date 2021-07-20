import numpy as np
import cv2, sys
from onnx_inference import movie_main
H, W = 1216, 1936


def run_camera(onnx_path_demo, video_path = 'driving.mov'):
    i=0 #frame counter
    if video_path:
        cap = cv2.VideoCapture(video_path)
    else:
        cap = cv2.VideoCapture(0)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        i +=1
        if i % 10 == 0:
            frame = cv2.resize(frame, (W, H))
            frame = movie_main(onnx_path_demo, frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    onnx_file_path = sys.argv[1]
    run_camera(onnx_file_path, video_path='driving.mov')
