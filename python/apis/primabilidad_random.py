import random


try:
    
    
    counter = (random.randint(0,1000g))
    def primos():
        for i in range(2, counter ):
            if counter % i == 0:
                print("El numero", counter, "NO es primo")
                break
        else:
            print("El numero", counter, " SI es primo")
    # for i in range (1,counter +1):
    #     print(i)
    #     if i % 2 == 0:
    #         print("No es primo")
    #     else:
    #         print("Es primo")
        
    
    # print (validation, counter)
    
    # def primos():
    #     if validation != 0:
    #         print(f"El número {counter} SI un número primo")
    #     elif counter == 2 or counter == 3 or counter == 5 or counter == 7:
    #         print(f"El número {counter} SI un número primo")

    #     else:
    #         print(f"El número {counter} NO es Primo")

    if __name__ == "__main__":
        primos()


except Exception as e:
    print(e)
             