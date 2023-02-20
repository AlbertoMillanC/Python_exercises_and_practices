#prime numebers 

num=int(input("Ingresa numero "))
primo=True

for n in range(2,num):
    if num % n == 0:
        print(f"No es un numero primo {n} no es divisor" )
        primo=False
        break
if primo:
    print("es primo")
    
        
        
        