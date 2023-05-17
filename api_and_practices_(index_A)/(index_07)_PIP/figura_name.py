ancho = 21  # ancho del cuadro en puntos
alto = 9  # alto del cuadro en puntos

# bucle para imprimir el cuadro de puntos
for i in range(alto):
    for j in range(ancho):
        if i == alto // 2 and j >= (ancho - len("Alberto Millán")) // 2 and j < (ancho - len("Alberto Millán")) // 2 + len("Alberto Millán"):
            # Imprime el nombre "Alberto Millán" en la fila central del cuadro
            print("Alberto Millán"[j - (ancho - len("Alberto Millán")) // 2], end=" ")
        else:
            # Imprime un punto
            print(".", end=" ")
    # Imprime un salto de línea después de cada fila
    print()
