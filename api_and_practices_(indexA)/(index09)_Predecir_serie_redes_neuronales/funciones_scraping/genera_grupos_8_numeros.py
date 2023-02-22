with open("C:\\Users\\ASUS\\Desktop\\datos_del_sorteo_comas_modificado.txt", "r") as archivo_original:
    contenido = archivo_original.read()
    contenido_modificado = '\n'.join([contenido[i:i+8] for i in range(0, len(contenido), 8)])

with open("archivo_modificado.txt", "w") as archivo_modificado:
    archivo_modificado.write(contenido_modificado)
