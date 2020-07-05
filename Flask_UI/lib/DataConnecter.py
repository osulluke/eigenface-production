class DataConnecter:
    
    """
    This class provides an interface to the image datastore (whether SQLite3 or MySQL).


    Attributes:
        imageDataStore:     connectionObject

    Methods:
        insertImage(_ID, _image):   none
        RetrieveImages():           Image[]
    """

    def __init__(self):
        """
        Initialization of DataConnecter object
        """

    def insertImage(self, _id, _image):
        """
        Called to insert an image into the database; only insert grayscale images

            Parameters:
                _id (int): ID# of image
                _image(Image):  Image to be inserted

            Returns:
                None
        """

    def RetrieveImages(self):
        """
        This function will retrieve all the images in the database in order to calculate
        or re-calculate the FaceSpace Matrix.

            Parameters:
                None

            Returns:
                allImages (Image[]): an array of all the images in the database
        """