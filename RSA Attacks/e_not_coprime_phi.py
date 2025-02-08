#taken from
#https://github.com/HackThisSite/CTF-Writeups/blob/master/2017/EasyCTF/RSA%204/README.md
#small modifications according to need

from Crypto.Util.number import GCD
import sympy

p = 0x9026329b302a421b04f81f2e95b9b1d429a2048ed19ca82e4a94c289402bcd7f3eb6685a505fa96898dfcd1fe1bfcb0dc14a47a04456499c35c44997301ee5a681835bbb1886a6871e24921223fd4c6e72459e4e3766b89b53a7716a1bb8ec12134cce4092804f518b07b246350edb1905d8c4f640a4edbc94c5fc1624aa5ea7
q = 0xa4a867734bd3c9802630644dbb273bdb978a807e841c6b96afa6e7603299226d3ff993b009cb15d7a735960d2ea1abc75c7bd1c0f2ce4de7041c2a251aa43da2bd842fd8abee860161003101a8d9b4bcc5803d727ac4ae16e287c8687154fba3c47279f0496d6e6e5331f38e2b26d9a8270eb6c225eaf2db5299009c0ef2d887
e = 0x65536
enc = 0x1a9c8fb7e55a7661f54f6cc0a5ae290373c5ae1d862196b487692cc17f42c956b7f718cfc065d924b6fa8ff90102146bfed65041eac27a9d56db350d8a6c963b591f22bc23714e38110ff5ee4ea1505f7fb79f81012b35e59f4d38e43f667e732b9539b6dc7be3b1c9d357f9e6b2685383e0b898b7f9b59d2484f7c9367e462772747606f534102d7c90b645eaf08969e7129b2f54b5a40ed26494997269b32322ea84f51eb6e2337e8513409f218a7c98be97d037766aa7bb6fa63989d3c2331269b17597ef60f93b895ffe6d7033d6d083a5732452f1f4049bf4bfc2caa1263a04a72ec18f338b199350f7322d851e589bc422c97b3fdf8ec08751b584019b
def invalidPubExponent(c,p,q,e):

    totientN = (p-1)*(q-1)
    n = p*q
    gcd = GCD(e,totientN)
    if(gcd == 1):
        return "[X] This method only applies for invalid Public Exponents."
    d = pow(e//gcd, -1, totientN)
    c = pow(c,d,n)
    plaintext = sympy.root(c,gcd)
    return plaintext
    
print(invalidPubExponent(enc, p, q, e))