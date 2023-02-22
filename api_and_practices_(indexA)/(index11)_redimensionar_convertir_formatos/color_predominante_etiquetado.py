import os
from PIL import Image, ImageDraw, ImageFont

folder = r"C:\Users\ASUS\Downloads\Photos"
size = (500,500)

for filename in os.listdir(folder):
    if filename.endswith(".jpg"):
        image = Image.open(os.path.join(folder, filename))
        image = image.resize(size)

        # Calcular el color predominante
        colors = image.getcolors(image.size[0]*image.size[1])
        most_frequent_color = colors[0][1]
        color_name = None
        # Asignar un nombre al color predominante
        if most_frequent_color == (255, 255, 255):
            color_name = "blanco"
        elif most_frequent_color == (0, 0, 0):
            color_name = "negro"
        elif most_frequent_color == (255, 0, 0):
            color_name = "rojo"
        elif most_frequent_color == (0, 255, 0):
            color_name = "verde"
        elif most_frequent_color == (0, 0, 255):
            color_name = "azul"

        # Agregar marca de agua con el nombre del color
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 36)
        textwidth, textheight = draw.textsize(color_name, font)
        draw.text((image.size[0]-textwidth-10, image.size[1]-textheight-10), color_name, font=font)

        image.save(os.path.join(folder, filename))
