from Crypto.Util.Padding import pad,unpad
from Crypto.Util.number import bytes_to_long,long_to_bytes
BLOCK_SIZE = 16
msg=b'davinci|rm=1'
msgPad=pad(msg, BLOCK_SIZE)
print(msgPad[:11]+(long_to_bytes(bytes_to_long(msgPad[11])^'4'^'1')))
print(msgPad)
print(b'09')
print(hex(bytes_to_long(msgPad)))

text="18e77a06d9e4a377835f7b9d90b60c9aa9f70130bade4e659c6c4f8a2852a83b"
#print(len(text))
