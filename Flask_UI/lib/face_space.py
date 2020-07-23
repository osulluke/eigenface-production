import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import Normalizer


class face_space:
    
    """
    This class the the "heart" of the project; it will query an
    image database to collect all the characters face images, create
    the PCA/SVD breakdown of the faces in the database along with

    Attributes:
        faceSpaceMatrix:        Principal Components Analysis of all the faces
        characterAverage[]:     Array of average character vectors

    Methods:
        _convert_raw_data():        initialize data for training
        CreateFaceSpace():          matrix/SVD/PCA
        ProjectFace(Vector):        Vector
        EuclideanDistance(Vector):  [(_FaceID, Double)]
        ReturnFaceIdentity(Vector): (_FaceID, _probability, _newFaceFlag)
    """

    def __init__(self):
        """
        Initialization of FaceSpace object
        """
        self.data_connection = data_connector()
        self.training_data_frame = retrieve_images()
        #self.training_data_frame = self.training_data_frame.set_index(0) # Preprocessing step to normalize data
        self.X = self.training_data_frame.drop(0, axis = 1) # Break out the image data only
        self.X.iloc[:,:] = Normalizer(norm='max').fit_transform(self.X) # Normalize the pixels
        self.Y = self.training_data_frame[0] # Break out the face IDs only
        self.create_face_space()


    def create_face_space(self):
        """
        Called with __init__(self); runs code that will build the face space "matrix"; can also be
        called 'on demand' after a certain number of new images have been added to the database,
        signaling the opportunity to train a new matrix and identify new faces.

            Parameters:
                None

            Returns:
                faceSpace (matrix/SVD/PCA): this is the data that represents the notion of "faceSpace" (fundamental)
        """
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.X, self.Y, train_size=.85)
        self.pca = PCA(n_components=110).fit(self.x_train)
        self.x_train_pca = self.pca.transform(self.x_train)
        #self.face_classifier = SVC().fit(self.x_train_pca, self.y_train)
        self.face_classifier = LinearDiscriminantAnalysis(solver='svd').fit(self.x_train, self.y_train)
        self.face_probability = SVC(probability=True).fit(self.x_train_pca, self.y_train)


    def project_face(self, vec):
        """
        This function will take a vector (a vectorized image) and project it into "FaceSpace". This function is where
        we will make use of the first 125-150 "Principal Components" which are generally used to identify faces.

            Parameters:
                vec (Vector): vector (of image) to be projected into FaceSpace

            Returns:
                projVec (Vector): vector projection of image into FaceSpace
        """


    def euclidean_distance(self, proj_vec):
        """
        Calculates the n-dimentional distance between the input vector and the average
        of all characters' vectors in FaceSpace. This will return an array of tuples 
        containing the ID of the character and the distance of projVec sorted in ascending
        order; the smallest distances will be the face that is most similar to the face
        represented by projVec.

            Parameters:
                proj_vec (Vector): vector projection of new face into FaceSpace

            Returns:
                dist_vec (Array (_id, _dist)): array of tuples (_id, _dist)
        """


    def return_face_identity(self, _id, _vec):
        """
        This function looks at the distance between known faces and uses some logic (TBD) to determine 
        whether or not a face has been identified; if it is new, it sends a message back to the FaceTester
        class to mark the face as such.

            Parameters:
                _id (int):     id# of image vector
                _vec (Vector): vector of image

            Returns:
                idVec (_id, bool, newFaceFlag): tuple representing the _id, probability, and whether it's a new face
        """


if __name__ == "__main__":
    face_space = face_space()
    face_space.x_test_pca = face_space.pca.transform(face_space.x_test)
    face_space.predictions = face_space.face_classifier.predict(face_space.x_test)
    print(classification_report(face_space.y_test, face_space.predictions))
