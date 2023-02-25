import os
from PIL import Image

folder = r"C:\Users\ASUS\Downloads\Photos"
size = (240,200)

for filename in os.listdir(folder):
    if filename.endswith(".jpg"):
        image = Image.open(os.path.join(folder, filename))
        image = image.resize(size)
        new_filename = filename.split(".jpg")[0] + "_resized.jpg"
        image.save(os.path.join(folder, new_filename))