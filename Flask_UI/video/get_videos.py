import sys
sys.path.append("..")
from filestore import *

videolist = get_s3objectList("videos/")

for video in videolist["Key"]:
    print(video)