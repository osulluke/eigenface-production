import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import Normalizer
from .data_connector import data_connector, retrieve_images, get_name_string
from collections import Counter


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
        aggregate_prediction():     determines the best prediction for a give face
    """

    def __init__(self):
        """
        Initialization of FaceSpace object
        """
        self.NORMALIZER = 255.0
        self.PREDICTION_THRESHOLD = 2
        self.data_connection = data_connector()
        self.training_data_frame = retrieve_images()
        self.X = self.training_data_frame.drop(0, axis = 1) # Break out the image data only
        self.X = (self.X.astype('int32')) / (self.NORMALIZER)
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
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.X, self.Y, train_size=.75)
        self.pca = PCA(n_components=135).fit(self.x_train)
        self.x_train_pca = self.pca.transform(self.x_train)
        param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
        self.face_classifier_lda = LinearDiscriminantAnalysis(solver='svd').fit(self.x_train, self.y_train)
        self.face_classifier_lda_pca = LinearDiscriminantAnalysis(solver='svd').fit(self.x_train_pca, self.y_train)
        self.face_classifier_svc_pca = SVC().fit(self.x_train_pca, self.y_train)
        self.face_classifier_svc_grid_pca = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid ).fit(self.x_train_pca, self.y_train)
        self.face_classifier_gnb_pca = GaussianNB().fit(self.x_train_pca, self.y_train)
        self.face_classifier_dec_tree_pca = tree.DecisionTreeClassifier().fit(self.x_train_pca, self.y_train)
        self.face_classifier_rfc_pca = RandomForestClassifier(n_estimators=18).fit(self.x_train_pca, self.y_train)
        self.face_classifier_knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean').fit(self.x_train, self.y_train)

    def aggregate_prediction(self, face_image):
        # Transform the face into a workable array
        transform_face = np.resize(face_image, (64,64))
        face_array = np.array(transform_face).ravel()
        face_array = [face_array / self.NORMALIZER]

        # Project the face image into "principal compoenents" / Eigenfaces
        face_PCA = self.pca.transform(face_array)

        # Make predictions using LDAs
        face_lda = self.face_classifier_lda.predict(face_array)
        face_lda_pca = self.face_classifier_lda_pca.predict(face_PCA)

        # Make preditions using SVC
        face_svc = self.face_classifier_svc_pca.predict(face_PCA)
        face_svc_grid = self.face_classifier_svc_grid_pca.predict(face_PCA)

        # Make predictions using GNB
        face_gnb = self.face_classifier_gnb_pca.predict(face_PCA)

        # Make predictions decision tree
        face_tree = self.face_classifier_dec_tree_pca.predict(face_PCA)

        # Make predictions random forest
        face_forest = self.face_classifier_rfc_pca.predict(face_PCA)

        # Make predictions using KNN
        face_knn = self.face_classifier_knn.predict(face_array)

        # Create an array of all the predictions
        counter = Counter()
        predictions = [face_lda, face_lda_pca, face_svc, face_svc_grid, face_gnb, face_tree, face_forest, face_forest, face_knn]

        # Determine the most common predictions
        for p in predictions:
            name = get_name_string(p[0])
            counter[name] += 1

        most_common = counter.most_common(2)
        try:
            if most_common[0][1] - most_common[1][1] >= self.PREDICTION_THRESHOLD:
                return most_common[0][0]
            else:
                return "UNKNOWN"
        except:
            return ""

if __name__ == "__main__":
    face_space = face_space()
    face_space.x_test_pca = face_space.pca.transform(face_space.x_test)
    face_space.predictions = face_space.face_classifier.predict(face_space.x_test)
    #face_space.predictions = face_space.face_classifier.predict(face_space.x_test_pca)
    face_space.predictions_ld = face_space.face_classifier_ld.predict(face_space.x_test_pca)
    face_space.knn_predictions = face_space.face_neighbors.predict(face_space.x_test)
    face_space.gnb_predictions = face_space.gnb.predict(face_space.x_test)
    print(classification_report(face_space.y_test, face_space.predictions))
    print(classification_report(face_space.y_test, face_space.predictions_ld))
    print(classification_report(face_space.y_test, face_space.knn_predictions))
    print(classification_report(face_space.y_test, face_space.gnb_predictions))
