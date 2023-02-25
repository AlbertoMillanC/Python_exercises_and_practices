with open("datos_del_sorteo2.txt", "r") as archivo_original:
    contenido = archivo_original.read()
    contenido_modificado = contenido.replace(",\n", "\n")

with open("red_datos_final_txt.txt", "w") as archivo_modificado:
    archivo_modificado.write(contenido_modificado)
