#Taken from
#https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Using_the_Chinese_remainder_algorithm

from Crypto.Util.number import getPrime, GCD
from functools import reduce

m = 1337 
 
p = getPrime(1024)
q = getPrime(1024)
n = p * q

e = 0x10001
phi = (p-1)*(q-1)

c = pow(m, e, n)
d = pow(e, -1, phi)

dp = d % (p-1)
dq = d % (q-1)
qinv = pow(q, -1, p)

m1 = pow(c, dp, p)
m2 = pow(c, dq, q)

h = qinv*(m1-m2) % p
m = m2 + (h*q)%n

assert m == 1337

