from Crypto.Cipher import AES
from aes import *

def xor(a, b):
    return bytes([i ^ j for i, j in zip(a, b)])

def get_blocks(data, block_size=16):
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]

def pad(plaintext):
    padding_len = 16 - (len(plaintext) % 16)
    padding = bytes([padding_len] * padding_len)
    return plaintext + padding

def unpad(plaintext):
    padding_len = plaintext[-1]
    assert padding_len > 0
    message, padding = plaintext[:-padding_len], plaintext[-padding_len:]
    assert all(p == padding_len for p in padding)
    return message

class ECB:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        """
        Plaintext: [P1, P2, P3, ...]
        Encrypted Blocks: [C1, C2, C3, ...]

        1. For each plaintext block:
           - C1 = Encrypt(Key, P1)
           - Encrypted Blocks: [C1]

        2. Continue encrypting the remaining blocks:
           - C2 = Encrypt(Key, P2)
           - Encrypted Blocks: [C1, C2]
           - C3 = Encrypt(Key, P3)
           - Encrypted Blocks: [C1, C2, C3]
           - ...

        3. Join the encrypted blocks to obtain the ciphertext:
           - Ciphertext: C1 + C2 + C3 + ...
        """
        plaintext = pad(plaintext)
        blocks = get_blocks(plaintext)
        encrypted_blocks = []
        for block in blocks:
            encrypted_block = encrypt(self.key, block)
            encrypted_blocks.append(encrypted_block)
        return b"".join(encrypted_blocks)

    def decrypt(self, ciphertext):
        """
        Ciphertext: [C1, C2, C3, ...]
        Decrypted Blocks: [P1, P2, P3, ...]

        1. For each ciphertext block:
           - P1 = Decrypt(Key, C1)
           - Decrypted Blocks: [P1]

        2. Continue decrypting the remaining blocks:
           - P2 = Decrypt(Key, C2)
           - Decrypted Blocks: [P1, P2]
           - P3 = Decrypt(Key, C3)
           - Decrypted Blocks: [P1, P2, P3]
           - ...

        3. Join the decrypted blocks to obtain the original plaintext:
           - Original Plaintext: P1 + P2 + P3 + ...
        """
        blocks = get_blocks(ciphertext)
        decrypted_blocks = []
        for block in blocks:
            decrypted_block = decrypt(self.key, block)
            decrypted_blocks.append(decrypted_block)
        return unpad(b"".join(decrypted_blocks))

class CBC:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
    def encrypt(self, plaintext):
        """
        Plaintext: [P1, P2, P3, ...]
        Encrypted Blocks: [C1, C2, C3, ...]

        1. Start with IV and P1:
           - C1 = Encrypt(Key, P1 ^ IV)
           - Encrypted Blocks: [C1]

        2. For the remaining blocks:
           - C2 = Encrypt(Key, P2 ^ C1)
           - Encrypted Blocks: [C1, C2]
           - C3 = Encrypt(Key, P3 ^ C2)
           - Encrypted Blocks: [C1, C2, C3]
           - ...

        3. Join the encrypted blocks to obtain the ciphertext:
           - Ciphertext: C1 + C2 + C3 + ...
        """
        plaintext = pad(plaintext)
        blocks = get_blocks(plaintext)
        encrypted_blocks = []
        encrypted_blocks.append(encrypt(self.key, xor(blocks[0], self.iv)))
        blocks = blocks[1:]
        for block in blocks:
            encrypted_blocks.append(encrypt(self.key, xor(block, encrypted_blocks[-1])))
        return b"".join(encrypted_blocks)
    def decrypt(self, ciphertext):
        """
        Ciphertext: [C1, C2, C3, ...]
        Decrypted Blocks: [P1, P2, P3, ...]

        1. Start with IV and C1:
           - Decrypt(C1) ^ IV = P1
           - Decrypted Blocks: [P1]

        2. For the remaining blocks:
           - Decrypt(C2) ^ P1 = P2
           - Decrypted Blocks: [P1, P2]
           - Decrypt(C3) ^ P2 = P3
           - Decrypted Blocks: [P1, P2, P3]
           - ...

        3. Join the decrypted blocks to obtain the original plaintext:
           - Original Plaintext: P1 + P2 + P3 + ...
        """
        blocks = get_blocks(ciphertext)
        decrypted_blocks = []
        decrypted_blocks.append(xor(decrypt(self.key, blocks[0]), self.iv))
        for i in range(1, len(blocks)):
            decrypted_block = xor(decrypt(self.key, blocks[i]), blocks[i - 1])
            decrypted_blocks.append(decrypted_block)
        return unpad(b"".join(decrypted_blocks))
        

key = b"A"*16
iv = b"B"*16
message = b"C"*31

cipher = CBC(key, iv)
aes = AES.new(key, AES.MODE_CBC, iv)

assert cipher.encrypt(message) == aes.encrypt(pad(message))


cipher = ECB(key)
aes = AES.new(key, AES.MODE_ECB)

assert cipher.encrypt(message) == aes.encrypt(pad(message))
