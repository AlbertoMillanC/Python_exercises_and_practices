import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import img2pdf

folder = r"C:\Users\ASUS\Downloads\Photos"

width = int(input("Enter the width: "))
height = int(input("Enter the height: "))
size = (width, height)

new_folder = r"C:\Users\ASUS\Downloads\Resized Photos"
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

images = []
for filename in os.listdir(folder):
    if filename.endswith(".jpg"):
        image = Image.open(os.path.join(folder, filename))
        image = image.resize(size)
        new_filename = filename.split(".jpg")[0] + "_resized.jpg"
        image.save(os.path.join(new_folder, new_filename))
        images.append(image)

with open(os.path.join(new_folder, "resized_photos.pdf"), "wb") as f:
    f.write(img2pdf.convert(images))
