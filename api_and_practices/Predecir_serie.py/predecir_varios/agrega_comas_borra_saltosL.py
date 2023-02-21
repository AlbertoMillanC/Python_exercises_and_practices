with open("C:\Users\ASUS\Desktop\Python_exercises_and_practices\Python_exercises_and_practices\datos_boyaca.txt", "r") as archivo:
    contenido = archivo.read().replace("\n", " ")
    print(contenido)
