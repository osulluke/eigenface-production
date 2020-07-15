import cv2
import random
import string
from mysql import connector
import pandas as pd
from urllib.parse import unquote

config = {
'user': 'admin',
'password': 'ohmypycis4930',
'host': "ohmypy.cdd0llcf03hp.us-east-1.rds.amazonaws.com",
'port': '3306',
'database': 'metadata',
'raise_on_warnings': True}

mydb = connector.connect(**config)


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
        sql_select_query = "select concat(f.name_id,  ',', convert(f.face_vector USING utf8)) as face_vector from name_data n join face_data f on f.name_id = n.name_id;"
        cursor = mydb.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        df = pd.DataFrame(records)

        return df

if __name__ == "__main__":
    data_connector = DataConnector()

    print(data_connector.RetrieveImages())