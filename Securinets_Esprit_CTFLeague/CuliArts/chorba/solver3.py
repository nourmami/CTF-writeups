#!/usr/bin/env python3
import os
from pwnlib.tubes.remote import remote
from codecs import encode,decode
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes

r = remote("127.0.0.1", 10000)
r.recvuntil(b"this level: ")
cipher = r.recvline().strip()
cipher = decode(cipher, "hex")
print("***************cipher**************")
print(cipher)

def xor(ch1,ch2):
    return bytearray(a ^ b for a, b in zip(ch1,ch2))


def split_blocks(data):
    length=len(data)
    blocks = []
    for i in range(length//16):
        blocks.append(data[i*16:(i+1)*16])
    return blocks


def find_bytes(blocks):
    C1 = bytearray([b for b in blocks[0]]) #copy of block0 of the ciphertext= IV
    
    plaintext_bytes = bytearray([0 for _ in range(16)])  #the correct plaintext array of  bytes initialized to zeros 

    for i in range(16):

        print("**************",i,"**************")
        expected_padding=bytearray([0 for _ in range(16-i-1)]+[(i+1)for _ in range(i+1)])
        print(expected_padding)
        C1 = xor(xor(expected_padding,plaintext_bytes),blocks[0])

        for byte in range(0,256):
            print("**************",byte,"**************")

            C1[15-i]=byte    #change the padding for i=0 C1[15]=byte
            to_test=bytes((C1+blocks[1])) #to_test=C1(block[0]+block[1])
            r.recvuntil(b"> ") 
            r.sendline(b"1")
            r.recvuntil(b" (hex): ")
            r.sendline(to_test.hex())
            r.recvuntil(b"layka_'s opinion: ")
            test = r.recvline().strip()
            print(test)
            if(test==b'Delicious'):
                plaintext_bytes[15-i]=(byte^(i+1)^blocks[0][15-i])
                break
            else:
                pass

        print("**************","plaintext","**************")

        print(plaintext_bytes.hex())
    return(bytes(plaintext_bytes))

def find_plaintext(cipher):
    blocks=split_blocks(cipher)
    print(blocks)
    plaintext=b""
    for i in range(len(blocks)- 1):
        plaintext+=find_bytes(blocks[i:i+2])

    print(plaintext)




find_plaintext(cipher)

