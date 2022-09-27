
#los multiplos de 2, 3, 5, 7 no son primos. el restante si lo es. de
import random


try:
   
    class Show:

        def __or__(self,primo):
            for i in range(1):
                print (random.randrange(0 ,10000))
        
    
    a= Show()
    b = a % 2 and a % 3 and a % 5 and a % 7
   
    
    def primos():
        if b != 0:
            print("Primos")                      
        else:
            print("Primos incorrect")
            
   
    
    
    if __name__ == "__main__":
        primos()
        
    
     
                  
except:
    print("Failed to interrupt")
    
                    
                    

                