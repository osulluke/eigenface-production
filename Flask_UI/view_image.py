from lib import get_test, insert_face, face_space, get_name_string
import cv2
import numpy as np
from PIL import Image
import sys

np.set_printoptions(threshold=sys.maxsize)

df = get_test()
i = 0

face_space = face_space()

for index, row in df.iterrows():
    y = [int(i) for i in row[1].split(',')]
    shape = (64,64)

    image_arr = np.asarray(y)
    image_arr = image_arr.reshape(shape)
    im = Image.fromarray(image_arr,'L')
    image = image_arr.astype(np.uint8)

    shape = (4096,1)
    image_arr = image_arr.reshape(shape)

    im = im.resize((64, 64))
    im_array = np.array(im).ravel()
    im_array = im_array / im_array.max()

    trans_arr = [im_array]
    prediction = face_space.face_classifier.predict(trans_arr)
    print(prediction)
    name = "Prediction: " + get_name_string(prediction[0])

    cv2.imshow(name, image)
    cv2.waitKey()