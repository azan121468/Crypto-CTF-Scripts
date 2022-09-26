from Crypto.Util.number import GCD, bytes_to_long, long_to_bytes

def encrypt(msg):
    print(f"Encrypt this message => {msg}")
    while True:
        try:
            print("Enter encrypted message :", end="")
            enc = int(input())
            break
        except ValueError:
            continue
    return enc

def get_input():
    msg_to_sign = input()
    while msg_to_sign == '':  #User must enter a message to sign
        print("Enter message to sign : ", end='')
        msg_to_sign = input()
    if msg_to_sign[-1] == " ":
        #if msg has space in end then it is treated as string integer
        # "1337" is treated as 1337    ==> integer
        # "1337 " is treated as "1337" ==> string
        try:
            msg_to_sign = int(msg_to_sign[:-1]) #remove last character(which is space)
            return str(msg_to_sign).encode(), msg_to_sign
        except:
            #If after stripping value cannot be converted to integer
            msg_to_sign = msg_to_sign.encode()
            return msg_to_sign, bytes_to_long(msg_to_sign)
    else:   #If message did not end with space
        try:
            msg_to_sign = int(msg_to_sign)
            return long_to_bytes(msg_to_sign), msg_to_sign
        except ValueError:
            msg_to_sign = msg_to_sign.encode()
            return msg_to_sign, bytes_to_long(msg_to_sign)
            
print("Can Server sign negative values : ", end="")
n_val = input() or True
if n_val.lower() == "yes" or n_val.lower() == "y" or n_val == "-1":
    #This part has no confirmations of correctness of modulus because less messages are encrypted. Be Careful
    while True:
        try:
            enc_n_1 = encrypt(-1)
            n = enc_n_1 + 1
            print(f"[+] Modulus : {n}")
            
            msg_to_sign = {}
            print("Enter message to sign : ", end='')
            msg_to_sign["bytes"], msg_to_sign["long"] = get_input()
                    
            if msg_to_sign["long"] == 0:
                print("Exiting")
                exit(0)
            
            print("[+] Message to sign(bytes) => %s"%format(msg_to_sign["bytes"]))
            print("[+] Message to sign(long)  => %s"%format(msg_to_sign["long"]))
            print(f"[+] Message to sign(hex)  => %s"%format(hex(msg_to_sign["long"])))
                
            enc_n_msg_to_sign = encrypt(-msg_to_sign["long"])
            
            if -enc_n_msg_to_sign >= 0 or (n - enc_n_msg_to_sign) <= 0:
                #Sometime script gives both singed message negative
                #This is if modulus is wrong
                print("[-] Incorrect Modulus")
                print("Try Again")
                continue
            
            print(f"[+] Message to sign(bytes) => %s"%format(msg_to_sign["bytes"]))
            print(f"[+] Message to sign(long)  => %s"%format(msg_to_sign["long"]))
            print(f"[+] Message to sign(hex)  => %s"%format(hex(msg_to_sign["long"])))
            print(f"[+] Signed Message(negative) => {-enc_n_msg_to_sign}")
            print(f"[+] Signed Message(positive) => {n-enc_n_msg_to_sign}")
            print(f"[+] Signed Message(hex) => {hex(n-enc_n_msg_to_sign)}")
        except Exception as e:
            print(f"[-] Exception : {e}")
            continue    
else:   #If server cannot sign negative values
    #Using RSA homomorphic property
    #    2 * 3 = 6
    #    7 * 5 = 35
    enc_2  = encrypt(2)
    enc_3  = encrypt(3)
    enc_6  = encrypt(6)
    enc_5  = encrypt(5)
    enc_7  = encrypt(7)
    enc_35 = encrypt(35)

    val1 = (enc_2 * enc_3) - enc_6
    val2 = (enc_5 * enc_7) - enc_35

    n = GCD(val1, val2)

    try:
        assert (enc_2 * enc_3) % n == enc_6
        assert (enc_5 * enc_7) % n == enc_35
    except AssertionError:
        print("[-] Cannot find modulus")
        exit(0)
    except Exception as e:
        print(f"[-] Exception : {e}")
        exit(0)
        
    print(f"[+] Modulus : {n}")
    
    ##Todo:
    #Bruteforce e to recover public key
    #for i in range(65537):
    #    if pow(2, i, n) == enc_2:
    #        e = i
    #        print(f"[+] E : {e}")
    #        break

    while True:
        try:
            msg_to_sign = {}
            print("Enter message to sign : ", end='')
            msg_to_sign["bytes"], msg_to_sign["long"] = get_input()
            
            if msg_to_sign["long"] == 0:
                print("Exiting")
                exit(0)
            
            print("[+] Message to sign(bytes) => %s"%format(msg_to_sign["bytes"]))
            print("[+] Message to sign(long)  => %s"%format(msg_to_sign["long"]))
            print("[+] Message to sign(hex)  => %s"%format(hex(msg_to_sign["long"])))

            enc_msg_to_sign_2 = encrypt(msg_to_sign["long"] * 2)
            signed_msg = (enc_msg_to_sign_2 * pow(enc_2, -1, n)) % n
            
            print(f"[+] Message to sign(bytes) => %s"%format(msg_to_sign["bytes"]))
            print(f"[+] Message to sign(long)  => %s"%format(msg_to_sign["long"]))
            print(f"[+] Message to sign(hex)  => %s"%format(hex(msg_to_sign["long"])))
            print(f"[+] Signed Message(long) => {signed_msg}")
            print(f"[+] Signed Message(hex) => {hex(signed_msg)}")
        except Exception as e:
            print(f"[-] Exception : {e}")
            continue