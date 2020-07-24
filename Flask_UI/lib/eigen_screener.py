import cv2
import sys
import time

from .tv_watcher import tv_watcher
from .data_connector import data_connector
from .face_processor import face_processor
from .face_space import face_space
from .stream_controller import stream_controller

class eigen_screener:

    """
    This class is a "composition" of other objects that are used to identify faces, control
    database access, control the video stream, and test faces that are found in the stream.

    Attributes:
        vid_stream:         the base video stream a user desires to watch
        tv_watcher:         A TV_Watcher() object
        data_connection:    A DataConnector() object
        face_processor:     A FaceProcessor() object
        face_space:         A FaceSpace() object
        stream_controller:  A StreamController() object
    """
    
    def __init__(self):
        #self.vid_stream = cv2.VideoCapture(vid)
        self.tv_watcher = tv_watcher()
        self.data_connection = data_connector()
        self.face_processor = face_processor()
        self.face_space = face_space()
        self.stream_controller = stream_controller()


if __name__ == "__main__":
    eigen_screener = eigen_screener()
    
    video_stream = cv2.VideoCapture('../video/FinerThingsClub.mp4')
    while True:
        ret, frame = eigen_screener.tv_watcher.captureScreen(video_stream)
        if time.time() % 3 <= 1:
            eigen_screener.tv_watcher.scanForFaces(frame)
            print("# detected_faces = " + str(len(eigen_screener.tv_watcher.detected_faces)))

        if cv2.waitKey(30) & 0xFF == ord('q'): # https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
            break
        else:
            try:
                cv2.imshow('frame', frame)
            except:
                pass

    for im in eigen_screener.tv_watcher.detected_faces:
        eigen_screener.data_connection.insertImage(_image=im, _id=None)
        cv2.imshow('frame', im)
        cv2.waitKey(30)

    cv2.waitKey()
    cv2.destroyAllWindows()