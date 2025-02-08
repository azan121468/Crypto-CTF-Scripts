#https://blog.redrocket.club/2018/03/27/VolgaCTF-Forbidden/
#this blog link the the github gist from where i copied the script
#https://gist.github.com/rugo/c158f595653a469c6461e26a60b787bb

"""
VolgaCTF Quals 2018 forbidden crypto task
This implements the forbidden attack on Galois/Counter Mode AES
useage: sage -python forb_expl.py
"""
from binascii import unhexlify, hexlify
from sage.all import *


def slice_and_pad(b_str, bsize=16):
    b_str += "\x00" * (len(b_str) % bsize)
    return [bytearray(b_str[k:k+bsize]) for k in range(0, len(b_str), bsize)]


def unhex_blocks(h_str, bsize=16):
    h_str = unhexlify(h_str)
    return slice_and_pad(h_str, bsize)

def xor(a, b):
    assert(len(a) == len(b))
    return bytearray([a[i] ^ b[i] for i in range((len(a)))])

def byte_to_bin(byte):
    b = bin(byte)[2:]
    return "0" * (8 - len(b)) + b

def block_to_bin(block):
    assert(len(block) == 16)
    b = ""
    for byte in block:
        b += byte_to_bin(byte)
    return b

def bytes_to_poly(block, a):
    f = 0
    for e, bit in enumerate(block_to_bin(block)):
        f += int(bit) * a**e
    return f        

def poly_to_int(poly):
    a = 0
    for i, bit in enumerate(poly._vector_()):
        a |= int(bit) << (127 - i)
    return a

def poly_to_hex(poly):
    return (hex(poly_to_int(poly))[2:-1]).upper()

C1 = unhex_blocks("1761e540522379aab5ef05eabc98516fa47ae0c586026e9955fd551fe5b6ec37e636d9fd389285f3")
T1 = unhex_blocks("0674d6e42069a10f18375fc8876aa04d")
A1 = slice_and_pad("John Doe")

C2 = unhex_blocks("1761e540522365aab1e644ed87bb516fa47ae0d9860667d852c6761fe5b6ec37e637c7fc389285f3")
T2 = unhex_blocks("cf61b77c044a8fb1566352bd5dd2f69f")
A2 = slice_and_pad("VolgaCTF")

C3 = unhex_blocks("1761e540522379aab5ef05eabc98516fa47ae0d9860667d852c6761fe5b6ec37e646a581389285f3")
A3 = slice_and_pad("John Doe")

# Same length for all messages
bit_len_plain = len(C1) / 2 * 8
bit_len_auth = len("John Doe") * 8
L = unhex_blocks(hex((bit_len_auth << 64) | bit_len_plain)[2:-1])


T = xor(T1[0], T2[0])
C = [
    xor(C1[0], C2[0]),
    xor(C1[1], C2[1]),
    xor(C1[2], C2[2])
]
A = xor(A1[0], A2[0])

# Sage magic

F, a = GF(2**128, name="a").objgen()
R, X = PolynomialRing(F, name="X").objgen()

A1_p = bytes_to_poly(A1[0], a)
C1_p = [
    bytes_to_poly(C1[0], a),
    bytes_to_poly(C1[1], a),
    bytes_to_poly(C1[2], a)
]
T1_p = bytes_to_poly(T1[0], a)

A3_p = bytes_to_poly(A3[0], a)
C3_p = [
    bytes_to_poly(C3[0], a),
    bytes_to_poly(C3[1], a),
    bytes_to_poly(C3[2], a)
]

A_p = bytes_to_poly(A, a)
C_p = [
    bytes_to_poly(C[0], a),
    bytes_to_poly(C[1], a),
    bytes_to_poly(C[2], a)
]
T_p = bytes_to_poly(T, a)

L_p = bytes_to_poly(L[0], a)



f1 = A1_p * X**5 + C1_p[0] * X**4 + C1_p[1] * X**3 + C1_p[2] * X**2 + L_p * X + T1_p
f3 = A3_p * X**5 + C3_p[0] * X**4 + C3_p[1] * X**3 + C3_p[2] * X**2 + L_p * X
p = A_p * X**5 + C_p[0] * X**4 + C_p[1] * X**3 + C_p[2] * X**2 + T_p

for root, _ in p.roots():
    EJ = f1(root)
    flag = f3(root) + EJ
    print("VolgaCTF{" + poly_to_hex(flag) + "}")
