import os
from PIL import Image, ImageDraw, ImageFont
import datetime

folder = r"C:\Users\ASUS\Downloads\Photos"
size = (500,500)
watermark_text = input("Ingrese el texto de la marca de agua: ")

font = ImageFont.truetype("arial.ttf", 36)

for filename in os.listdir(folder):
    if filename.endswith(".jpg"):
        image = Image.open(os.path.join(folder, filename))
        image = image.resize(size)
        
        draw = ImageDraw.Draw(image)
        textwidth, textheight = draw.textsize(watermark_text, font)
        position = (size[0] - textwidth - 10, size[1] - textheight - 10)
        draw.text(position, watermark_text, font=font, fill=(255, 255, 255, 128))
        
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        textwidth, textheight = draw.textsize(current_time, font)
        position = (size[0] - textwidth - 10, size[1] - textheight - 50)
        draw.text(position, current_time, font=font, fill=(255, 255, 255, 128))
        
        new_filename = filename.split(".jpg")[0] + "_resized_with_watermark_and_time.jpg"
        image.save(os.path.join(folder, new_filename))
