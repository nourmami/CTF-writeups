from pwn import *
from codecs import encode,decode
from Crypto.Util.number import long_to_bytes


host = '20.203.26.7'
port = 10007

t = remote(host, port)

flag=""
for i in range(15,2,-2):
    print("*****************",i,"*****************")
    payload = b"0"*i+str.encode(flag)
    print("*****************payload",payload)
    t.recvuntil(b"> ")
    t.sendline(b"2")
    t.recvuntil(b" (hex): ")
    t.sendline(payload.hex())
    t.recvuntil(b" ready:")
    cipherPartialFlag = t.recvline().strip()
    cipherPartialFlag = decode(cipherPartialFlag, "hex")
    cipherPartialFlag = cipherPartialFlag[0:16]
    print(cipherPartialFlag)

    for i in range(0, 256):
        t.recvuntil(b"> ")
        t.sendline(b"1")
        t.recvuntil(b" (hex): ")
        t.sendline(payload.hex()+long_to_bytes(i).hex())
        t.recvuntil(b" ready:")
        cipherTest = t.recvline().strip()
        cipherTest = decode(cipherTest, "hex")
        
        if cipherTest[0:16] == cipherPartialFlag:
            flag += (long_to_bytes(i).hex())
            print("Flag: ", flag)
            break
print(flag)
11111111111111111111111111111111
e57c4a7d038241030dddac27fe443132
c3c7d03f1e173b9822806ed91d35769c
