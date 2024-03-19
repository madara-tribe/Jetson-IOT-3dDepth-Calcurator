import argparse
import sys, os
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QDockWidget
from qtWidgets.RightCamWidget import RightCamWidget
from qtWidgets.LeftWidget import LeftWidget
from onnx_inference import image_main, movie_main
import cv2

class MyMainWindow(QMainWindow):
    def __init__(self, opt, parent=None):
        super(MyMainWindow, self).__init__(parent)
        
        # RIGHT Side camera widget
        here_path = os.path.dirname(os.path.abspath(__file__))
        self.plot_layout = QVBoxLayout()
        self.right_video_path = os.path.join(here_path, opt.right_video_path)
        self.right_widget = RightCamWidget(self, self.right_video_path, opt.onnx_path)
        self.plot_layout.addWidget(self.right_widget)
        self.setCentralWidget(self.right_widget)
        
        
        # Left side widget
        cap = self.right_widget.return_cap()
        self.leftDock = QDockWidget("Left Widget", self)
        self.leftside = LeftWidget(self, cap)
        self.leftDock.setWidget(self.leftside)
 
        self.leftDock.setAllowedAreas(Qt.LeftDockWidgetArea
                                   | Qt.RightDockWidgetArea)
        self.leftDock.setFeatures(QDockWidget.DockWidgetMovable
                                  | QDockWidget.DockWidgetFloatable \
                                  #|QDockWidget.DockWidgetVerticalTitleBar)
                                  )
        self.addDockWidget(Qt.LeftDockWidgetArea, self.leftDock)
        
def run_camera(onnx_path, video_path):
    H, W = 1216, 1936
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
            frame = movie_main(onnx_path, frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--qtapp', action='store_true', help='Use Pyside6 GUI Display on mac')
    parser.add_argument('--inference', action='store_true', help='onnx inference to single image')
    parser.add_argument('--camera', action='store_true', help='onnx movie inference without GUI display')
    parser.add_argument('--height', type=int, default=480, help='height of movie')
    parser.add_argument('--width', type=int, default=640, help='width of of movie')
    parser.add_argument('--right_video_path', type=str, default='data/Rdriving.mov', help='right side camera video_path')
    parser.add_argument('--onnx_path', type=str, default='data/yolov4_1_3_416_416_static.onnx', help='onnx file path')
    parser.add_argument('--image_path', type=str, default='data/images/train_2007.jpg', help='image file path')
    opt = parser.parse_args()
    return opt
 
def main(opt):
    if opt.qtapp:
        app = QApplication(sys.argv)
        # app.setStyle(QStyleFactory.create('Cleanlooks'))
        w = MyMainWindow(opt)
        w.setWindowTitle("PySide Layout on QMainWindow")
        w.resize(opt.width, opt.height)
        w.show()
        sys.exit(app.exec_())
    elif opt.inference:
        image_main(opt.onnx_path, opt.image_path)
    elif opt.camera:
        run_camera(onnx_path=opt.onnx_path, video_path=opt.right_video_path)
 
if __name__ == '__main__':
    opt = get_parser()
    main(opt)
