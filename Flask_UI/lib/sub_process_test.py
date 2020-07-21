import time
from PIL import ImageGrab
import numpy as np
import cv2
from face_space import face_space
from tv_watcher import tv_watcher
from eigen_screener import eigen_screener
i = 0

eigen_screener = eigen_screener()

while True:    
    time.sleep(2)
    print("i = ", str(i))
    i += 1
    im = ImageGrab.grab()
    im = np.array(im)
    eigen_screener.tv_watcher.scanForFaces(im)

    for face in eigen_screener.tv_watcher.detected_faces:
        t_face = np.resize(face, (64,64))
        face_arr = np.array(t_face).ravel()
        face_arr = [face_arr / face_arr.max()]
        print("Prediction: ", eigen_screener.face_space.face_classifier.predict(face_arr))
        
    eigen_screener.tv_watcher.detected_faces.clear()
