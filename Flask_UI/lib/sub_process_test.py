import time
from PIL import ImageGrab
import numpy as np
import cv2
from face_space import face_space
from tv_watcher import tv_watcher
from eigen_screener import eigen_screener
from data_connector import get_name_string
i = 0

eigen_screener = eigen_screener()

while True:
    time.sleep(0.5)
    print("i = ", str(i))
    i += 1
    im = ImageGrab.grab()
    im = np.array(im)
    eigen_screener.tv_watcher.scanForFaces(im)

    for face in eigen_screener.tv_watcher.detected_faces:
        t_face = np.resize(face, (64,64))
        face_arr = np.array(t_face).ravel()
        NORMALIZER = 255.0
        face_arr = [face_arr / NORMALIZER]
        face_pca = eigen_screener.face_space.pca.transform(face_arr)
        prediction = eigen_screener.face_space.face_classifier.predict(face_arr)[0]
        probability = eigen_screener.face_space.face_probability.predict(face_pca)
        character_name = get_name_string(prediction)
        print("Prediction:", character_name, "ID:", prediction)
        print("Probability:", get_name_string(probability[0]), "ID:", probability)
        
    eigen_screener.tv_watcher.detected_faces.clear()
    # Code to determine if commerical or not
    # Code to activate or deactivate the mute (Selenium call)
