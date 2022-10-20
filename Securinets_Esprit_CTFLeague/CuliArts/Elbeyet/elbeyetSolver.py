#!/usr/bin/env python3

from pwnlib.tubes.remote import remote
from codecs import decode
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

#P1=IV ^AES(key,C1)
#P2=C1 ^AES(key,C2)
#C1=C2=00000000000000000000000000000000
#P1^P2=IV

r = remote("20.203.26.7", 10009)
r.recvuntil(b"anymore: ")
cipher = r.recvline().strip()
cipher = decode(cipher, "hex")
#print(cipher
r.recvuntil(b"> ") #00000000000000000000000000000000
r.sendline(b"1")
r.recvuntil(b" (hex): ")
r.sendline(b"0000000000000000000000000000000000000000000000000000000000000000")
r.recvuntil(b"Mekla Mjamra: ")
p1p2 = r.recvline().strip()
print(p1p2)   
r.close
#print(IVB)
p1p2 = decode(p1p2, "hex")
p1=p1p2[0:16]
print("*******",p1)
p2=p1p2[16:32]
print("*******",p2)
#print(p1p2)
IV=bytes(a ^ b for a, b in zip(p1,p2))
print("*******",IV)

BLOCK_SIZE = 16
KEY = IV  

def jammer_elbeyet(data):
    aes_cipher = AES.new(KEY, AES.MODE_CBC, IV)
    return aes_cipher.decrypt(data)

print(jammer_elbeyet((cipher)))

