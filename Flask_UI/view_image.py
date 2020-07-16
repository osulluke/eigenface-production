from db_functions import get_test, set_name, insert_face
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

df = get_test()
i = 0

for index, row in df.iterrows():
    id = row[0]
    y = [int(i) for i in row[1].split(',')]
    shape = (64,64)

    image_arr = np.asarray(y)
    image_arr = image_arr.reshape(shape)
    im = Image.fromarray(image_arr,'L')
    image = image_arr.astype(np.uint8)
    cv2.imshow("Faces found", image)
    cv2.waitKey()

    #name = input("Enter name: ")
    #set_name(id, name)
    #insert_face(row[1], name)
