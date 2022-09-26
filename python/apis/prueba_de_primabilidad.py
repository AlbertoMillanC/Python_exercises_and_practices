#los multiplos de 2, 3, 5, 7 no son primos. el restante si lo es. de


correct_passworks = (17)

def primos():
    n= int(input("input your numbers "))
    for i in (range(0,120,2)):      
        for j in (range(0,120,3)):
            for k in (range(0,120,5)):
                for l in (range(0,120,7)):
                    yield 
                    
for(i,j,k,l) in primos():
        if(i,j,k,l) == correct_passworks:
            print ("Is correct your password ")
            print(i,j,k,l)
            continue
                    
                    

                