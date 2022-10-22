#"// crear lista de números primos"?
def isprime(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False

# valores = []
# while True:
#     try:
#         valor = 1 , 4 ,47, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173,
#         if valor == 0:
#             break
#         valores.append(valor)
#     except ValueError:
#         print("Inserta un número.")

# print(valores)           
        
# primos=[]
# for valor in valores:
#     if isprime(valor):
#         primos.append(valor)
# if primos:
#     print("Los numeros primos son: ", primos)

# else:
#     print("Ningún número ingresado es un número primo") 



# import random
# import timeit

# try:

#     for num in range(1,10):
#         if num > 1:
#             cont=0
#             i = 2
#             while i<num and cont==0:
#                 resto = num%i
#                 if resto == 0:
#                     cont == 1
#                 i +=1
#             if cont == 0:
#                 print(num)


# except :
#     print("e")
             