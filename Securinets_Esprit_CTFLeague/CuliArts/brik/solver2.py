from pwnlib.tubes.remote import remote
from codecs import encode,decode
from Crypto.Util.number import long_to_bytes


host = '127.0.0.1'
port = 10007

t = remote(host, port)


flag=""
for i in range(15,0,-1):
    print("*****************",i,"*****************")
    payload = "00"*(i)+(flag)
    print("*****************payload",payload)
    t.recvuntil(b"> ")
    t.sendline(b"2")
    t.recvuntil(b" (hex): ")
    print("*****************test1",str.encode(payload))
    t.sendline(str.encode(payload))
    t.recvuntil(b" ready:")
    cipherPartialFlag = t.recvline().strip()
    cipherPartialFlag = cipherPartialFlag[:32]
    print(cipherPartialFlag)

    for i in range(0, 256):
        print("testing",i)
        t.recvuntil(b"> ")
        t.sendline(b"1")
        t.recvuntil(b" (hex): ")
        test=payload+(long_to_bytes(i).hex())
        t.sendline(str.encode(test))
        print("*****************test2",str.encode(test))

        t.recvuntil(b" ready:")
        cipherTest = t.recvline().strip()
        print(cipherTest[:32])
        if cipherTest[:32] == cipherPartialFlag:
            flag += (long_to_bytes(i).hex())
            print("Flag: ", flag)
            break
print(flag)
