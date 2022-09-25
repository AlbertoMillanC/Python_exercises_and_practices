#"//how   make  a funtion  with   python?"?

def saludo():
    yield "saludo"
    yield "hola"
    yield "qué tal"
    yield "Alberto"
    
def generate_numbers():
    for d1 in range(10):
            for d2 in range(10):
                    for d3 in range(10):
                        yield (d1,d2,d3)


