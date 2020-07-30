import time
from PIL import ImageGrab
import numpy as np
import cv2
#from face_space import face_space
#from tv_watcher import tv_watcher
from .eigen_screener import eigen_screener
from .data_connector import get_name_string
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

def run_face_screener():
    NORMALIZER = 255.0
    global eigen_screener 
    eigen_screener = eigen_screener()
    firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    firefox_driver.get('http://127.0.0.1:5000/')

    while True:
        try:
            #mute_button = firefox_driver.findElement(By.id("muteButton"))
            test = firefox_driver.find_element(By.TAG_NAME, 'video')
        except:
            print("\n***BUTTON NOT FOUND***\n")
            pass
        time.sleep(0.5)
        print(firefox_driver.current_url)
        im = ImageGrab.grab()
        im = np.array(im)
        eigen_screener.tv_watcher.scanForFaces(im)


        print('*****************************')
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

            #print("Prediction:", get_name_string(prediction[0]), "ID:", prediction)
            #print("Probability:", get_name_string(probability[0]), "ID:", probability)
            #print("Gaussian:", get_name_string(gaussian[0]), "ID:", gaussian)
            
            print(get_name_string(prediction[0]))
            print(get_name_string(probability[0]))
            print(get_name_string(gaussian[0]))
            print(get_name_string(tree[0]))
            print(get_name_string(rfc[0]))
            print('-----------------------------')

        #print()
        eigen_screener.tv_watcher.detected_faces.clear()
        # Code to determine if commerical or not

        # Code to activate or deactivate the mute (Selenium call)
        #driver = webdriver.Chrome()
        #driver.set_script_timeout(15)
    #
        ## Getting our html link
        #url = "http://link"
        #driver.get(url)
    #
        #video = EC.visibility_of_element_loated(By.TAG_NAME, 'video')
        ## Ensuring that the commercial is initializing 
        #
        ## Getting commercial from Luke code that determine if commercial is true or not
        #if(commercial == "true"):
        #    driver.execute_script("argument[0].muted = true;", video)
        #
        #elif(commercial == "false"):
        #    driver.execute_script("argument[0].muted = false;", video)
    #

if __name__ == "__main__":
    run_face_screener()