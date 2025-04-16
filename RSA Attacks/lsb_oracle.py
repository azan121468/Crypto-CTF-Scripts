#copied from: https://github.com/jvdsn/crypto-attacks/blob/master/attacks/rsa/lsb_oracle.py and modified a bit.
#Since last byte returned by the oracle is wrong, we will bruteforce it locally.

def attack(N, e, c, oracle):
    def lsb_oracle(ciphertext):
        #Implement this according to scenario
        raise NotImplementedError
    """
    Recovers the plaintext from the ciphertext using the LSB oracle (parity oracle) attack.
    :param N: the modulus
    :param e: the public exponent
    :param c: the encrypted message
    :param oracle: a function which returns the last bit of a plaintext for a given ciphertext
    :return: the plaintext
    """
    left = 0
    right = N
    while right - left > 1:
        print(right - left)
        c = (c * pow(2, e, N)) % N
        if oracle(c) == 0:
            right = (right + left) // 2
        else:
            left = (right + left) // 2

    return int(right)

def attack2(n, e, c, oracle):
    # This code was use to solve Challenge "Twin Oracles" from HTB Cyber Apoclypse 2025
    # Original Code and Solution can be found at: 
    # https://github.com/hackthebox/cyber-apocalypse-2025/tree/main/crypto/Twin%20Oracles
    # Adding here just for reference
    def is_lsb_oracle():
        raise NotImplementedError

    low, high = 0, n - 1
    i = 0

    while high - low > 1:
        mid = (low + high) // 2
        if is_lsb_oracle():   # LSB: dec(c) % 2 == 0
            r = 1 << (i + 1)
            cc = (c * pow(r, e, n)) % n
            if oracle(cc) == 0:
                high = mid
            else:
                low = mid
        else:                  # dec > (n//2)
            r = 1 << i
            cc = (c * pow(r, e, n)) % n
            if oracle(cc) == 0:
                high = mid
            else:
                low = mid
        print(low, high)
        i += 1
    
    return low

n = ...
e = ...
c = ...

pt = attack(n, e, c, lsb_oracle)
#since last byte is not correct, we will bruteforce it locally 
for i in range(0xff+1):
    pt = pt >> 8 << 8 | i
    if pow(pt, e, n) == c:
        print(f'Found: {pt}')
        break
else:
    #this shouldn't be reachable. Just added this condition if it did
    print(f'pt: {pt}')
    breakpoint()