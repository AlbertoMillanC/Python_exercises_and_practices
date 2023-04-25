import pytesseract 
import sys
from pdf2image import convert_from_path
import os 

# Ruta del PDF
PDF_file =r"C:\Users\ASUS\Desktop\Python_exercises_and_practices\Python_exercises_and_practices\vdoc.pub_devising-theatre-a-practical-and-theoretical-handbook-1.pdf"

#Lista de las páginas del PDF 
pages = convert_from_path(PDF_file, 500) 

#Archivo de texto donde se almacenará el texto reconocido 
txt_file = "resultado.txt"

# Borra el archivo de texto si existe 
if os.path.exists(txt_file):
    os.remove(txt_file)

#Reconoce el texto usando OCR en cada página 
for page in pages: 
    text = pytesseract.image_to_string(page) 
    
    # Escribe el texto en el archivo 
    with open(txt_file, "a") as f: 
        f.write(text)