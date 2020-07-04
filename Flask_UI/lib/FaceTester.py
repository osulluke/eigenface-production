class FaceTester:

    """
    This is a class that will test 'scraped' images
    to see if they are actually faces; it also provides
    some utility functionality to assist with data
    maintenance and database insertion.

    Methods:
        testFace(Image) :        boolean
        vectorize(Image):        Vector
        convertGrayScale(Image): Image
    """

    def __init__(self):
        """
        Initialization of FaceTester object
        """

    def testFace(self, im):
        """
        Tests an image to see if there is actually a face present or not; the intent is to preven images that do not contain
        faces from being inserted into the database.

            Parameters:
                im (Image): image to test 

            Returns:
                isFace (boolean): True/False value whether or not image is actually a face
        """

    def vectorize(self, im):
        """
        Vectorizes a face image (only "True" faces) in order to be able to compare it to other faces in the "FaceSpace" Matrix

            Parameters:
                im (Image): image to vectorize

            Returns:
                imVec (Vector): vector representing image
        """

    def convertGrayScale(self, im):
        """
        Converts a color face image to greyscale; only greyscale images should be inserted into the database.

            Parameters:
                im (Image): image to convert

            Returns:
                grayIm (Image): grayscale image of a face
        """