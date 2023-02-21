import re

with open("archivo_modificado.txt", "r") as archivo:
    contenido = archivo.read()
    contenido_modificado = re.sub(r'\d', lambda x: f"{x.group(0)},", contenido)

with open("datos_del_sorteo2.txt", "w") as archivo_modificado:
    archivo_modificado.write(contenido_modificado)
    
    
print("terminado con exito" )