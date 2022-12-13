#  inf -inf

from cmath import inf
try:

    a = float (inf)
    b = float (-inf)

    print (a + b)
    print (a - b)
    print (a / b)
    print (a * b)
    
except :
    print ("Error type")

