
#los multiplos de 2, 3, 5, 7 no son primos. el restante si lo es. de
try:
    i = 1
      
    a= int (input("input your number "))
    b = a % 2 and a % 3 and a % 5 and a % 7
   
    
    def primos():
        if b != 0:
            print("Primos")                      
        else:
            print("Primos incorrect")
            
    
    
                
        
    if __name__ == "__main__":
        primos()
        
    print(b)
     
                  
except:
    print("Failed to interrupt")
    
                    
                    

                