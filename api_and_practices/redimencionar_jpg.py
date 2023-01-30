import os
from PIL import Image

folder = r"C:\Users\ASUS\Downloads\Photos"
size = (500,500)

for filename in os.listdir(folder):
    if filename.endswith(".jpg"):
        image = Image.open(os.path.join(folder, filename))
        image = image.resize(size)
        image.save(os.path.join(folder, filename))