def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def long_to_bytes(m):
    return b"".fromhex(hex(m)[2:])

m = 0x41
n  = 
e1 = 
e2 = 
c1 = 
c2 = 

g, a1, a2 = egcd(e1, e2)
m = pow(c1, a1, n) * pow(c2, a2, n) % n
print(m)