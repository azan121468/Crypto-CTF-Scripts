import argparse
from Crypto.Util.number import long_to_bytes

def third_root(x):
    y, y1 = None, 2
    while y != y1:
        y = y1
        y3 = y ** 3
        d = (2 * y3 + x)
        y1 = (y * (y3 + 2 * x) + d // 2) // d
    return y

def main():
    parser = argparse.ArgumentParser(description="Calculate third_root of any large number")
    parser.add_argument('--number', help="Number of which you want to calculate cube root", type=int, default=None)
    args = parser.parse_args()
    if args.number is None:
        print("Simple Third root calculator")
        print("Usage: python 3rd_root.py --number <number>")
        exit()
    try:
        cube_root = third_root(args.number)
        if cube_root ** 3 == args.number:
            print(f"Cube Root: {cube_root}")
            print(f"Message  : {long_to_bytes(cube_root)}")
        else:
            raise
    except Exception:
        print("Cannot calculate cube root")
    
if __name__=="__main__":
    main()