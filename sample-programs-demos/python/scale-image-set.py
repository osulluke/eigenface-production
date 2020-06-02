from PIL import Image
import os

read_path = 'img/faces/scraped-faces/'
save_path = 'img/faces/scaled-faces/'
entries = os.listdir(read_path)
print(entries)

for f in entries:
    im = Image.open(read_path + f)
    im = im.resize((300,300))
    im.save(save_path + f)