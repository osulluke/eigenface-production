import time
from PIL import ImageGrab
import numpy as np
import cv2
from face_space import face_space
from tv_watcher import tv_watcher
from eigen_screener import eigen_screener
from selenium import webdriver
from selenium.webdriver.common.by import BY
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

i = 0

eigen_screener = eigen_screener()

while True:    
    time.sleep(1)
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
    # Code to determine if commerical or not

    # Code to activate or deactivate the mute (Selenium call)
    driver = webdriver.Chrome()
    driver.set_script_timeout(15)

    # Getting our html link
    url = "http://link"
    driver.get(url)

    video = EC.visibility_of_element_loated(By.TAG_NAME, 'video')
    # Ensuring that the commercial is initializing 
    driver.execute_async_script(
        var video = argument[0],
            callback = arguments[arguments.length -1]
        video.addEventListener('loadstart', listener)

        function listener(){
            callback()
        }, video
    )
    # Getting commercial from Luke code that determine if commercial is true or not
    if(commercial = "true"){
        driver.execute_script("argument[0].muted = true;", video)
    }
    elif(commercial = "false"){
        driver.execute_script("argument[0].muted = false;", video)
    }
