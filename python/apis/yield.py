#"//how   make  a funtion  with   python?"?

def saludo():
    yield "saludo"
    yield "hola"
    yield "qué tal"
    yield "Alberto"

correct_paswords= (3,5,6)
    
def generate_numbers():
    for d1 in range(10):
            for d2 in range(10):
                    for d3 in range(10):
                        yield (d1,d2,d3)
                        
                        
for(a,b,c) in generate_numbers():
    if(a,b,c) == correct_paswords:
        print ("Is correct your password ")
        print(a,b,c)
        break


