import os
from pathlib import Path
import re
from facedetect import facesquare, get_whole_image
from filestore import gettemp_cvimage
from db_functions import insert_face

dirname = Path(__file__).parents[2]
rootdir = os.path.join(dirname ,'faces')

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".jpg"):
            new_string = re.sub("\d", "", file)
            name = new_string.replace("_"," ").replace(".jpg","").strip()
            if "bj" in name:
                name = "B.J. Novak"

            image_file = gettemp_cvimage(filepath)
            image = get_whole_image(image_file)

            if image["num_face"] == 1:
                insert_face(image["gray_im"], name)