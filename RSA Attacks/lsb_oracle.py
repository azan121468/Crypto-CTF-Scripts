#copied from: https://github.com/jvdsn/crypto-attacks/blob/master/attacks/rsa/lsb_oracle.py and modified a bit.
#Since last byte returned by the oracle is wrong, we will bruteforce it locally.

def attack(N, e, c, oracle):
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

def lsb_oracle(ciphertext):
    #Implement this according to scenario
    raise NotImplementedError

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