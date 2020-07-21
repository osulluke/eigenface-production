import time
from PIL import ImageGrab
from face_space import FaceSpace
i = 0

while True:    
    time.sleep(2)
    print("i = ", str(i))
    i += 1
    im = ImageGrab.grab()

    im.show()