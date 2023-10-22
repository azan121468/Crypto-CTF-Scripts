from Crypto.Util.number import long_to_bytes
enc_flag = ? #enter your encrypted flag
enc_2 = ? #encrypt 2 from oracle
send = enc_flag * enc_2 #now multiply enc_2 and enc_flag
msg = int(input()) #then decrypt the resulting message
print(long_to_bytes(msg // 2)) #divide message by 2 to get flag
#encrypt flag
#encrypt 2
#multiply enc_2 and enc_flag
#then decrypt the resulting message
#divide message by 2 to get flag