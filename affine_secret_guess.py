import argparse

a = 0
b = 0

def enc(byte):
    return (a * byte + b) % 256
    
def encrypt_bytes(plain_bytes):
    enc_bytes = b""
    for i in plain_bytes:
        enc_bytes+=bytes([enc(i)])
    return enc_bytes

def main():
    global a, b
    parser = argparse.ArgumentParser(description="Guess secrets of Affine Cipher using known-plaintext attack")
    parser.add_argument('--file', help = "Encrypted file", type=str, default=None)
    parser.add_argument('--crib', help = "Known header of decrypted file(must be in hex)", type=str, default=None)
    parser.add_argument('--offset', help = "Offset from where start reading encrypted file", type=int, default=0)
    args = parser.parse_args()
    if args.file is None or args.crib is None or args.crib is None:
        print("Usage:")
        print("python affine.py --file <encrypted file> --crib <known bytes> --offset <offset of known bytes>")
        exit()
        
    try:
        args.crib = b"".fromhex(args.crib)
    except ValueError:
        args.crib = args.crib.encode()
    
    found = False
    with open(args.file, 'rb') as f:
        f.seek(args.offset)
        enc_content = f.read()[:len(args.crib)]

        for i in range(256):
            for j in range(256):
                a, b = i, j
                if encrypt_bytes(args.crib) == enc_content:
                    print("[+] Secrets found")
                    print(f"A : {a} B : {b}")
                    found = True
                    break
            if found:
                break
        
        if not found:
            print("[-] Secrets were not found.")

if __name__=="__main__":
    main()