from Crypto.Util.number import long_to_bytes

print("Encrypt this message => 2")
print("Enter encrypted message :", end="")
enc_2 = int(input())

while True:
    print("Enter encrypted flag :", end="")
    enc_flag = int(input())

    send = enc_flag * enc_2

    print(f"Decrypt this message => {send}")
    print("Enter decrypted message : ", end="")

    msg = int(input())
    msg //= 2

    print(f"Decrypted Message(long) : {msg}")
    print(f"Decrypted Message(bytes) : {long_to_bytes(msg)}")
    print(f"Decrypted Message(hex) : {long_to_bytes(msg)}")