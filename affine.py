import argparse

def decryption(msg, key1, key2):
    pt = []
    mod_val = 256
    for char in msg:
        char = char - key2
        val = pow(key1, -1, mod_val)
        char = val * char % mod_val
        pt.append(char)
    return bytes(pt)

def main():
    parser = argparse.ArgumentParser(description="XOR tool")
    parser.add_argument('--key1', help="first number", type=int, default=None)
    parser.add_argument('--key2', help="second number", type=int, default=None)
    parser.add_argument('--input', help="Encrypted file", type=str, default=None)
    parser.add_argument('--output', help="Output of decryption", type=str, default=None)
    args = parser.parse_args()
    
    if args.input is None or args.output is None or args.key1 is None \
                                                         or args.key2 is None:
        print("Usage:")
        print("python affine.py --input <file> --key1 <key1> --key2 <key2> --out <output file>")
        exit()
    
    x = open(args.input, 'rb').read()
    output = decryption(x, args.key1, args.key2)
    with open(args.output, 'wb') as f:
        f.write(output)
    

if __name__=="__main__":
    main()