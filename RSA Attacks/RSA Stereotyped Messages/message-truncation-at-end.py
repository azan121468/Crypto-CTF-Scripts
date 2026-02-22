from Crypto.Util.number import getPrime, bytes_to_long

msg = bytes_to_long(b"Here is the secret message which you will never be able to find : youcantseemypassword")

N = getPrime(1024) * getPrime(1024)
e = 3

print(f"{N=}")
print(f"enc = {pow(msg, e, N)}")
