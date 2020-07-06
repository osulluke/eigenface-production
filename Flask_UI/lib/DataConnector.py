import cv2
import random
import string

class DataConnector:
    
    """
    This class provides an interface to the image datastore (whether SQLite3 or MySQL). Currently it is set up to work using the file system since a database is not yet implemented.


    Attributes:
        imageDataStore:             connectionObject

    Methods:
        insertImage(_ID, _image):   none
        RetrieveImages():           Image[]
    """

    def __init__(self):
        """
        Initialization of DataConnector object
        """

        self.data_location = 'fake_database/'
        self.letters = string.ascii_letters

    def insertImage(self, _id, _image):
        """
        Called to insert an image into the database; only insert grayscale images

            Parameters:
                _id (int): ID# of image
                _image(Image):  Image to be inserted

            Returns:
                None
        """

        if _id == None:
            temp_id = ''.join(random.choice(self.letters) for i in range(6))
            cv2.imwrite(self.data_location + temp_id + '.jpg', _image)
        else:
            pass

        return

    def RetrieveImages(self):
        """
        This function will retrieve all the images in the database in order to calculate
        or re-calculate the FaceSpace Matrix.

            Parameters:
                None

            Returns:
                allImages (Image[]): an array of all the images in the database
        """

if __name__ == "__main__":
    data_connector = DataConnector()