from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes, isPrime

flag = bytes_to_long(b"SuperSecretMessage")

e = getPrime(128)
while True:
  p, q = getPrime(512), getPrime(512)
  if (p-1) % e and (q-1) % e:
    break

n = p * q
d = pow(e,-1,(p-1)*(q-1))

pubkey = (n, e)
privkey = (n, d)

def encrypt(message, pubkey=pubkey):
    n, e = pubkey
    return pow(message, e, n)
    
def decrypt(message, privkey=privkey):
    n, d = privkey
    return pow(message, d, n)

enc_flag = encrypt(flag, pubkey)
enc_2 = encrypt(2, pubkey)

assert decrypt(enc_flag * enc_2) // 2 == flag
assert decrypt(enc_flag * enc_2) == flag * 2
assert (encrypt(2) * encrypt(flag)) % n == encrypt(flag * 2)
assert decrypt(encrypt(flag) * encrypt(2)) == decrypt(encrypt(flag * 2))