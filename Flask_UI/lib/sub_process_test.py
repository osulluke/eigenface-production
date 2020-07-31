import time
from PIL import ImageGrab
import numpy as np
import cv2
from .eigen_screener import eigen_screener
from .data_connector import get_name_string
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import random

def run_face_screener():
    NORMALIZER = 255.0
    global eigen_screener 
    eigen_screener = eigen_screener()
    video_player = ""
    state = "SHOW"
    firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())#, firefoxOtions=firefox_options)
    firefox_driver.get('http://127.0.0.1:5000/')

    while True:
        time.sleep(0.5)
        try:
            video_player = firefox_driver.find_element_by_id('video_player') # Access video player element
        except:
            print("\n***VIDEO PLAYER NOT FOUND***\n") # print message if no video play is present

        # Get the current screen shot and capture faces
        im = ImageGrab.grab()
        im = np.array(im)
        eigen_screener.tv_watcher.scanForFaces(im)

        print('*****************************')

        # Identify faces that have been captured
        for face in eigen_screener.tv_watcher.detected_faces:
            t_face = np.resize(face, (64,64))
            face_arr = np.array(t_face).ravel()
            face_arr = [face_arr / NORMALIZER]
            
            face_pca = eigen_screener.face_space.pca.transform(face_arr)
            prediction = eigen_screener.face_space.face_classifier.predict(face_arr)
            probability = eigen_screener.face_space.face_probability.predict(face_pca)
            gaussian = eigen_screener.face_space.gnb.predict(face_pca)
            tree = eigen_screener.face_space.dec_tree.predict(face_pca)
            rfc = eigen_screener.face_space.rfc.predict(face_pca)
            
            print(get_name_string(prediction[0]))
            print(get_name_string(probability[0]))
            print(get_name_string(gaussian[0]))
            print(get_name_string(tree[0]))
            print(get_name_string(rfc[0]))
            print('-----------------------------')

            if random.randint(0, 10) < 12:
                state = "COMMERCIAL"    
            else:
                state = "SHOW"

        eigen_screener.tv_watcher.detected_faces.clear()

        # Mute the show based 'state' of the show (COMMERCIAL or SHOW)
        if video_player != "":
            if state == "SHOW":
                firefox_driver.execute_script("arguments[0].muted = false;", video_player) # Unmute the player
            elif state == "COMMERCIAL":
                firefox_driver.execute_script("arguments[0].muted = true;", video_player) # Mute the player

if __name__ == "__main__":
    run_face_screener()