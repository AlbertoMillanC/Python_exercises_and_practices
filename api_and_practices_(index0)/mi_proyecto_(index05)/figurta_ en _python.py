import shutil

def dibujar_arbol(altura, mensaje):
    
  # Dibuja un árbol de Navidad con un mensaje en el centro
  # La altura del árbol es la cantidad de líneas que tiene

  # Calcula el ancho de la pantalla
  ancho_pantalla = shutil.get_terminal_size().columns

  # Calcula el ancho del árbol
  ancho_arbol = int(ancho_pantalla * 0.8)

  # Calcula el número de espacios a la izquierda del árbol
  espacios = (ancho_pantalla - ancho_arbol) // 2

  for i in range(altura):
    # Dibuja espacios a la izquierda del árbol
    for j in range(espacios):
      print(" ", end="")
    # Dibuja ramas del árbol
    for j in range(2 * i + 1):
      print("*", end="")
    # Salto de línea al final de cada fila
    print()

  # Dibuja el mensaje en el centro del árbol
  espacios = (ancho_pantalla - len(mensaje)) // 2
  for i in range(espacios):
    print(" ", end="")
  print(mensaje)

# Ejemplo de uso: dibuja un árbol de altura 22 con el mensaje "Feliz Navidad"
dibujar_arbol(22, "Feliz Navidad")
