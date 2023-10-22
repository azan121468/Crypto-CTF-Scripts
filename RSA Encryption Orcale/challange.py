from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes, isPrime

flag = b"SuperSecretMessage"

e = getPrime(128)
while True:
  p, q = getPrime(512), getPrime(512)
  if (p-1) % e and (q-1) % e:
    break

n = p * q
d = pow(e,-1,(p-1)*(q-1))

pubkey = (n, e)
privkey = (n, d)

def encrypt(message, pubkey):
    n, e = pubkey
    return pow(message, e, n)
    
def decrypt(message, privkey):
    n, d = privkey
    return pow(message, d, n)

enc_flag = encrypt(bytes_to_long(flag), pubkey)

while True:
    print("1) Encrypt message")
    print("2) Decrypt message")
    print("3) Get Flag")
    print("Enter your option : ",end="")
    opt = int(input())
    if opt == 1:
        print("Enter message you want to encrypt:", end="")
        msg = int(input())
        print(f"Encrypted message => {encrypt(msg, pubkey)}")
    elif opt == 2:
        print("Enter message you want to decrypt:", end="")
        msg = int(input())
        if msg % n == enc_flag:
            print("You cannot decrypt flag")
            continue
        print(f"Decrypted message => {decrypt(msg, privkey)}")
    elif opt == 3:
        print(f"Encrypted flag => {enc_flag}")