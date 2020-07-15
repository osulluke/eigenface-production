import numpy as np
from PIL import Image
from FaceSpace import FaceSpace

def file_vector(string):
    im = Image.open(string).convert('L')
    im = im.resize((64,64))
    im_array = np.array(im).ravel()

    return im_array

if __name__ == "__main__":
    face_space = FaceSpace()
    while True:
        print("Input an image string to test; exit with 'q': ")
        img_string = input()
        if img_string == 'q':
            break
        else:
            file_string = 'fake_database/' + img_string
            im_array = file_vector(file_string)
            trans_arr = face_space.pca.transform([im_array])
            prediction = face_space.face_classifier.predict(trans_arr)
            print("Prediction:", prediction, "\n")

    print("Thanks for checking this out...")
