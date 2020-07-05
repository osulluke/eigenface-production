class FaceProcessor:

    """
    This is a class that will test 'scraped' images
    to see if they are actually faces; it also provides
    some utility functionality to assist with data
    maintenance and database insertion.

    Attributes:
        faceArray(Image[]):      array of chopped face images
        databaseConnection:      connection to the DataConnecter object

    Methods:
        orientFace(Image):          Image
        convertGrayScale(Image):    Image
        vectorize(Image):           Vector
        foundNewFace(_id, Image):   none
    """

    def __init__(self):
        """
        Initialization of FaceProcessor object
        """

    def orientFace(self, im):
        """
        Re-orients a face image so that the features are generally algined; need eyes, nose, mouth, etc to all
        generally be in the same place in the image of a face.

            Parameters:
                im (Image): image to re-orient

            Returns:
                oriented_im (Image): Returns the re-oriented image so it is aligned properly
        """

    def convertGrayScale(self, im):
        """
        Converts a color face image to greyscale; only greyscale images should be inserted into the database.

            Parameters:
                im (Image): image to convert

            Returns:
                grayIm (Image): grayscale image of a face
        """

    def vectorize(self, im):
        """
        Vectorizes a face image (only executed on "True" faces) in order to be able to compare it to other faces in the "FaceSpace" Matrix

            Parameters:
                im (Image): image to vectorize

            Returns:
                imVec (Vector): vector representing image
        """

    def foundNewFace(self, _id, _im):
        """
        Called when a new face is found by the FaceSpace object; this will push that face image to the database.

            Parameters:
                _id (int): ID# of new face 
                im (Image): image to insert to database

            Returns:
                none
        """

if __name__ == "__main__":
    face_processor = FaceProcessor()