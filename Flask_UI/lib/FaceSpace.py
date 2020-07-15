import pandas as pd

class FaceSpace:
    
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

    def __init__(self, basic_data):
        """
        Initialization of FaceSpace object
        """
        self.raw_data_frame = pd.read_csv(basic_data)
        self.training_data_frame = ""
        self._convert_raw_data()

    def _convert_raw_data(self):
        num_faces = self.raw_data_frame.shape[0] # Number of rows in the dataframe

        # Loop over each row; replace with integer array
        for row in range(0, num_faces):
            s = self.raw_data_frame['face_vector'][row]
            numeric_data = s[s.find("[")+1:s.find("]")]
            numeric_data = ' '.join(numeric_data.split())
            arr = [int(i) for i in numeric_data.split(' ')]
            self.raw_data_frame['face_vector'][row] = arr

        # Initialize training data set
        self.training_data_frame = self.raw_data_frame

    def CreateFaceSpace(self):
        """
        Called with __init__(self); runs code that will build the face space "matrix"; can also be
        called 'on demand' after a certain number of new images have been added to the database,
        signaling the opportunity to train a new matrix and identify new faces.

            Parameters:
                None

            Returns:
                faceSpace (matrix/SVD/PCA): this is the data that represents the notion of "faceSpace" (fundamental)
        """

    def ProjectFace(self, vec):
        """
        This function will take a vector (a vectorized image) and project it into "FaceSpace". This function is where
        we will make use of the first 125-150 "Principal Components" which are generally used to identify faces.

            Parameters:
                vec (Vector): vector (of image) to be projected into FaceSpace

            Returns:
                projVec (Vector): vector projection of image into FaceSpace
        """

    def EuclideanDistance(self, projVec):
        """
        Calculates the n-dimentional distance between the input vector and the average
        of all characters' vectors in FaceSpace. This will return an array of tuples 
        containing the ID of the character and the distance of projVec sorted in ascending
        order; the smallest distances will be the face that is most similar to the face
        represented by projVec.

            Parameters:
                projVec (Vector): vector projection of new face into FaceSpace

            Returns:
                distVec (Array (_id, _dist)): array of tuples (_id, _dist)
        """

    def ReturnFaceIdentity(self, _id, _vec):
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
    face_space = FaceSpace("../../../faces/top10.csv")