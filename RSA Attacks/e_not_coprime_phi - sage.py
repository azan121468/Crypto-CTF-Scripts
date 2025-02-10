#taken and modified: https://ctftime.org/writeup/31122

from Crypto.Util.number import long_to_bytes

e = ...
p = ...
q = ...
c = ...

rmodp = (c % p).nth_root(e, all=True)
rq = (c % q).nth_root(e)

for rp in rmodp:
    r = crt(int(rp), int(rq), p, q)
    flag = long_to_bytes(r)

    if b"flag" in flag:
        print(flag.decode())