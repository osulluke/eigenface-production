class TV_Watcher:
    
    """
    This is a class that will 'watch' the TV stream, take a screen shot every so often (~1/sec); as
    different screens are captured, a face-detection algorithm will be run against the image and an 
    array of detected faces in that image will be formed; once the detected faces are found, they 
    will then be tested in order to ensure that an image does, in fact, contain a face, and this 
    array of faces will then be passed on to the next object.

    Attributes:
        video_stream:            Video stream data; base data

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

    def captureScreen(self, vid_stream):
        """
        Takes a screen capture of a video stream (~1/second)

            Parameters:
                vid_stream(Video):      Video stream

            Returns:
                screenCap (Image):      Image representing a slice of video data
        """

    def scanForFaces(self, im):
        """
        Runs a face detection algorithm on a scene (image) from the video stream and returns 
        an array containing all the "faces" that were detected.

            Parameters:
                im (Image):                 image to scan for faces

            Returns:
                detected_faces (Image[]):   array containing all of the image slices where faces were detected
        """

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
    tv_watcher = TV_Watcher()