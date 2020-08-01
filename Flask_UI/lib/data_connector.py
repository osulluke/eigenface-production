import cv2
import random
import string
from mysql import connector
import pandas as pd
from urllib.parse import unquote
import os
from pathlib import Path

config = {
'user': 'admin',
'password': 'ohmypycis4930',
'host': "ohmypy.cdd0llcf03hp.us-east-1.rds.amazonaws.com",
'port': '3306',
'database': 'metadata',
'raise_on_warnings': True}

mydb = connector.connect(**config)


class data_connector:
    
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


# return a dataframe of vectors nameid,pix1,pix2,pix3,...pix4096
def retrieve_images():
    sql_select_query = "select concat(f.name_id,  ',', convert(f.face_vector USING utf8)) as face_vector from name_data n join face_data f on f.name_id = n.name_id;"
    cursor = mydb.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    df = pd.DataFrame(records)
    df = pd.DataFrame([sub.split(",") for sub in df[0]])
    return df


def get_name_id(name):
    name = unquote(name)
    sql_select_query = "SELECT MIN(name_id) FROM name_data WHERE full_name = '" + name + "'"
    cursor = mydb.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()

    name_id = records[0][0]
    if name_id != None:
        return name_id
    else:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO name_data (full_name) VALUES ('" + name + "')")
        mydb.commit()
        cursor.close()
        return get_name_id(name)


def get_face_id(face_vector, name_id):
    sql_select_query = "SELECT MIN(face_id), count FROM face_data WHERE face_vector = '" + face_vector + "'"
    cursor = mydb.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()

    face_id = records[0][0]
    if face_id != None:
        new_count = records[0][1] + 1
        sql_select_query = "UPDATE face_data SET count = " + str(new_count) + " WHERE face_id = " + str(face_id) + ""
        cursor = mydb.cursor()
        cursor.execute(sql_select_query)
        mydb.commit()
        cursor.close()
        return face_id
    else:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO face_data (face_vector, name_id, count) VALUES ('" + face_vector + "',"+str(name_id)+", 1)")
        mydb.commit()
        cursor.close()
        return get_face_id(face_vector, name_id)


def get_face(face_vector):
    sql_select_query = "select n.full_name from name_data n join face_data f on f.name_id = n.name_id WHERE face_vector = '" + str(face_vector) + "'"
    cursor = mydb.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    row_count = cursor.rowcount

    if row_count == 0:
        return 'Not Found, please add face to database'
    else:
        name = records[0][0]
        return name


def get_name_string(name_id):
    sql_select_query = "select n.full_name from name_data n where n.name_id = " + name_id + ";"
    cursor = mydb.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    row_count = cursor.rowcount

    if row_count == 0:
        return 'Name not found'
    else:
        name = records[0][0]
        return name


def get_name(face_vector):
    sql_select_query = "select r.full_name from none_data r WHERE r.face_vector = '" + str(face_vector) + "'"
    cursor = mydb.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    row_count = cursor.rowcount

    if row_count == 0:
        return 'Not Found'
    else:
        name = records[0][0]
        return name


def scrape_face(face_vector):
    sql_select_query = "SELECT face_vector FROM none_data WHERE face_vector = '" + face_vector + "'"
    cursor = mydb.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    row_count = cursor.rowcount

    if row_count == 0:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO none_data (face_vector) VALUES ('" + face_vector + "')")
        mydb.commit()
        cursor.close()


if __name__ == "__main__":
    data_connector = data_connector()

    print(retrieve_images())