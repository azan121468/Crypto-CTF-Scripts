import argparse

xor = lambda a, b: b"".join([bytes([i ^ j]) for i, j in zip(a, b)])
    
def main():
    parser = argparse.ArgumentParser(description="XOR tool")
    parser.add_argument('--enc', help="HEX of Ciphertext", type=str, default=None)
    parser.add_argument('--crib', help="What you know about plaintext", type=str, default=None)
    args = parser.parse_args()

    if args.enc is None or args.crib is None:
        print("Please supply ciphertext and plaintext.")
        exit()
    ciphertxt = b"".fromhex(args.enc)
    crib = args.crib.encode()
    
    secret_key = xor(ciphertxt, crib)
    
    length = len(ciphertxt)//len(secret_key) + 1
    
    plain_text = xor(ciphertxt, secret_key * length)
    
    try:
        print(plain_text.decode())
    except UnicodeDecodeError:
        print(plain_text)

if __name__ == "__main__":
    main()