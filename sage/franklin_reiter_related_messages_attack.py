from sage.all import *
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime, inverse

"""
Find RSA encrypted message m.
c1 = encrypt(a1 * m + b1)
c2 = encrypt(a2 * m + b2)
Where (n, e) is RSA public key.
"""

n = 
e = 
c1 = 
a1 = 
b1 = 
c2 = 
a2 = 
b2 = 

def compositeModulusGCD(a, b):
    if(b == 0):
            return a.monic()
    else:
            return compositeModulusGCD(b, a % b)

def FranklinReiter(n, e, c1, c2, a1, a2, b1, b2):
    P.<x> = PolynomialRing(Zmod(n))
    f = (a1*x+b1)^e - c1
    g = (a2*x+b2)^e - c2
    m =  Integer(n-(compositeModulusGCD(f,g)).coefficients()[0])
    return m
    
print(long_to_bytes(FranklinReiter(n, e, c1, c2, a1, a2, b1, b2)))