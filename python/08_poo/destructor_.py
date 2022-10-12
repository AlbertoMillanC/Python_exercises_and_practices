from msilib.schema import Class


try:

    class Animales:

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def grupo(self):
            print("Nombre del grupo", self.name)

        def __del__(self):
            print("Se ha eliminado el objeto")
            
    animal = Animales("aves")
    animal.grupo()    
    del animal
    print(animal.name)

except Exception:
    print("Error")
    
finally:
    print("Fin del programa")
