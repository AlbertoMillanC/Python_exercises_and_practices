def new_func(n):
    i=0
    a=0
    while(i<n):
        a = a+i
        i = i+2
    return a
    
print (new_func(5))

    
   


try:

    new_func()
    
   
except :
    print("Hubo un error. Saliendo del programa")
   