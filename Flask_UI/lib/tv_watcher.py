# Source: https://github.com/shantnu/FaceDetect; modeled after this use case

import cv2
import sys
import time

class tv_watcher:
    
    """
    This is a class that will 'watch' the TV stream, take a screen shot every so often (~1/sec); as
    different screens are captured, a face-detection algorithm will be run against the image and an 
    array of detected faces in that image will be formed; once the detected faces are found, they 
    will then be tested in order to ensure that an image does, in fact, contain a face, and this 
    array of faces will then be passed on to the next object.

    Cascades downloaded from openCV GitHub repository: https://github.com/opencv/opencv/tree/master/data/haarcascades

    Attributes:
        video_stream:                    Video stream data; base data
        frontal_face_detector_default:   Haar cascade detector for frontal faces (default version)
        eye_cascade                      Haar cascade detector for eyes
        front_cascade_alt                Haar cascade alternate face detector (1)
        cascade_path_front_alt_2         Haar cascade alternate face detector (2)
        detected_faces                   Image array of faces that were detected

    Methods:
        captureScreen(VideoStream):     Image; screen capture of video stream
        scanForFaces(Image):            Image[]; image array containing detected faces
        filterOnlyFaces(Image[]):       Image[]; runs an algorithm on the image array to remove non-faces
        sendFaceArray(Image[]):         Image[]; sends the array of "actual" faces
    """

    def __init__(self):
        """
        Initialization of FaceTester object
        """

        # Create the primary frontal face detector
        self.front_cascade_default = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        # Create alternate detectors; to be used to help filter scraped images
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
        self.front_cascade_alt = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
        self.cascade_path_front_alt_2 = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")

        # Variables to convert the scene to grayscale and collect face slices
        self.gray_scene = ""
        self.x_start = 0
        self.x_end = 0
        self.y_start = 0
        self.y_end = 0

        # Variables to hold detected faces
        self.detected_faces = []

    def captureScreen(self, vid_stream):
        """
        Takes a screen capture of a video stream (~1/second)

            Parameters:
                vid_stream(Video):      Video stream

            Returns:
                screenCap (Image):      Image representing a slice of video data
        """
        ret, screenCap = vid_stream.read()

        return ret, screenCap

    def scanForFaces(self, image_scene):
        """
        Runs a face detection algorithm on a scene (image) from the video stream and returns 
        an array containing all the "faces" that were detected.

            Parameters:
                imamge_scene (Image):       image of total scene to scan for faces

            Returns:
                detected_faces (Image[]):   fills an array containing all of the image slices where faces were detected
        """

        # Take an initial hack at scanning an image for faces; these parameters work pretty well
        # self.gray_scene = cv2.cvtColor(image_scene, cv2.COLOR_BGR2GRAY), # cv2 relies on grayscale images; commented out b/c the 
        self.gray_scene = image_scene
        faces = self.front_cascade_default.detectMultiScale(
            self.gray_scene,
            scaleFactor = 1.3,
            minNeighbors = 6,
            minSize = (70, 70),
            flags = cv2.CASCADE_SCALE_IMAGE
        )

        # Loop over all the face rectangles found in the scene
        for (x, y, w, h) in faces:
            self.x_start = x
            self.y_start = y
            self.x_end = x + w
            self.y_end = y + h
            face = cv2.cvtColor(self.gray_scene[self.y_start:self.y_end, self.x_start:self.x_end], cv2.COLOR_RGB2GRAY)
            face = cv2.resize(face, (200,200), interpolation = cv2.INTER_AREA)
            self.detected_faces.append(face)

        return

    def filterOnlyFaces(self, im_array):
        """
        Takes an image array containing detected faces and tests each one to ensure that there is 
        actually a face present.

            Parameters:
                im_array (Image[]):         array of images containing possible faces

            Returns:
                act_faces (Image[]):        array containing only actual faces after they're tested
        """

    def sendFaceArray(self, im_array):
        """
        Sends the array of "actual" faces on for further processing

            Parameters:
                im_array (Image[]):         array of actual face images to send

            Returns:
                None
        """

if __name__ == "__main__":
    tv_watcher = tv_watcher()
    video_stream = cv2.VideoCapture('../video/FinerThingsClub.mp4')
    while True:
        ret, frame = tv_watcher.captureScreen(video_stream)
        if time.time() % 1 <= 1:
            tv_watcher.scanForFaces(frame)
            print("# detected_faces = " + str(len(tv_watcher.detected_faces)))

        if cv2.waitKey(30) & 0xFF == ord('q'): # https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
            break
        else:
            try:
                cv2.imshow('frame', frame)
            except:
                pass

    for im in tv_watcher.detected_faces:
        cv2.imshow('frame', im)
        cv2.waitKey(10)

    cv2.waitKey()
    cv2.destroyAllWindows()