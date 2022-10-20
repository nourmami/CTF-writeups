from Crypto.Util.number import long_to_bytes,inverse
from gmpy2 import iroot
from pwn import *
import math,json


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def hex_int(hex):
    return(int(hex,16))
    
def send_X(n):
    json_send({"x":n})
    return(recv(n))

host="20.65.65.163"
port=1003
r = remote(host,port)

#recieve N,c,e
r.recvuntil(")")
data=json_recv()
c=hex_int(data["encrypted_Flag"])
n=hex_int(data["N"])
e=hex_int(data["e"])
print(c,n,e)
#send x=3 and receive data3= p^3-q^3
data3=hex_int(send_X("3"))
#send x=4 and receive data4= p^4-q^4
data4=hex_int(send_X("4"))

#k=p-q
k=math.gcd(data4,data3)
#k1=p+q
k1=int(iroot((k**2)+(4*n),2)[0])
#k1=iroot(2*k1,2)[0]
phi=n-k1+1
d  = inverse(e,phi)
m = pow (c,d,n)
print(long_to_bytes(m))



#cHex="0xc33e39c61a816a2ddf9e140fea68a0949d43e5ef3cfd0ad464afcff0f0727e64d44323d51b24aa75a17fdca3cf655cd58faa41f4a441032bffea2cca1ff672f7af2c9cb282319b63e9fdc6d86a18ed79752711d5d94302fe8aa10cb75145085e0f9fb2a8674b49cbdf8b06513f7f022e21a4352178e1eb37e67cacdea403c85f61adff4bbbe03cc068c474ad1cd65fcc6e9cb4d0ccf00e319357a6033b2760ca68ab16ceb4ecad42f1b738d6c95c71507896d40bea4bea77f6cb1ef23ab07cd3f028a562c414810e90800a8aac62a3e7fe6fb240cb9922fd625e8d64ac5f013ce3ceb477ceeaa65854412700af94aeb1dd3a2c9adad44e2669a4709678258abb"
#c=int(cHex,16)
#eHex="0x10001"
#e=int(eHex,16)
#nHex="0xd08c6b2d14aae0e771d64cc07914526d3974022b2718417c6806b50873c3b75948c6ec8eef7c231b73270f973d8c7da6d6d2eea1152b4f49346ff724c044dafaead1796c673d6593241f995ee2f0a91cfbcfe2a1463d8eb9783e44d2600a3cdbf8db25bfcf06b447b549fdec299d1a8b2ef677c00011fe57b55f65f3de41ebb521b0da6daa505da76bbe3432ada388d24439314d7c73057ca754a64a5edcf23068ffa020a4f0e1659dbd11c6da2b0be01ad4bd765c9d88031255fa348a8c562cfc364e0dd05e69ce3bb2d418f4b3d692860adc3e17fadb9b881c315b4043136d12f66039fee51a3acb9a94496851770a5d6eba1100d7edf417d28d40d1e6ce97"
#n=int(nHex,16)
#k=p^3-q^3
#kHex="0x3a0d24c82db655ed80f58359c7eff814c9b67afb44d3c2b93193eee7be7351409b48055196ea13037cf7daa99371eece0a7e117fe50a31358ee73d55dd47c0d448d0c1a07c4e2546f32b6291198dd1294d346f1e2b215c7a4f335b60014d1f6a35f113289cb68cc30e6565cfe7818e197c76117689e11ac264e59f33530b483b9d75635b5d5c1de5ae4e7d904160ebbd203f1ff3e6decdfc366d281b9e5d9d47cf7351ef0b795ad870e0205a6d9634eb5179d8fc1260288d86735174d0e2e5f54b7fbf75eda258dcf5f4beb7d068a33b2f429ddab3cfc7816239a243936306f5190f4a319c413437ed9af4253230467059bc831df91ca58687018a9caead16162afe3ee4e34de3acd40690f45ce0aa80ce69004f85548b490dd2443a0fb8ae76848187c70f1f8e5272cb8cd2163186fed12c34d34a712857bb63dcfae9c196de79063ac208cd49e8b54b25b591e29f159f35a7e644327dd6ee5657b8c05b36da364ff66e8b7174ad86c7c42d4e735473e924f3622a8f60ab877215e51b132e06"
#k=int(kHex,16)
#g=p^5-q^5
#gHex="0x4f5ea80b795a600b000a408f459858b2742a3418760aab5f4755f3da7ae1707df78264b94d420b039cdd32a6ab4d853ec58fbc054287bd035a225500b3323c72179ffcf449ef6c55d7fdec563984f80cb20bb9a665b9c8295b41495780ee2f18c4901f2dabdaf875c04058ee90898912c46c57fc17c3f77d3e7a140f3e84ea3b75a7ef68aa0b2aa71ee25f0f65bc395375ce40fd4184763c7ee0b5487e7de287a02f1e71388c51ff135303cab1119bff886717f8989701830f3dccfaead40aa29439701a24ea9b4365479db70221640ebc67a57479f9829f6ed1febc247696c464e534b59cf3d1267398ede7a97d52f1aa5d8598e91a6ac14ff3fcaf75a0c0e5342ca1c37908711e0c2c0fa04588913d08d498ad2eafea65af79a733ee6ebc3bfafb38147653ed7a6f268f496ddd9d4868ffdeddadcd97a4e2e665f67a2faafd04bfa0d293e3b65ce3cfb17463bb7519060b34bf210f6165103e1831e884a2cc8a373738576b1f4981b09906405a2075e48daf880a30734eab7f142051384e4b4fd1c3aa2a3dec6a5382075c0992457309d33366cca0cecfc089b713ca1d9ac83439545371721b7c9d861ffe3c42fceae4ee96d175d8226e684d62b807765f23abf8ea6fa26a75b7a5f8d631c74fdd4db0abfad184f752f8e77acdd442ead93896839bad455b5a8ccf60ed715796eb3081bc0e8966f61374809740f26e577398441b2b540c1b636145bf963e4d88d7fed56ccac17131f0276e9bb0d83040442424ee4c1e2fb352108748d3b463ff454bb1e0a6135357979916736dc60d69dcb58a1ac52601e95f5d698bf9df83645032617b2fded9874c17600d4409ceced73938eb7e81d0b8d081f70f8e2a9b1f2e841a2270d6b6b5ae1ac05ad9c9e8251176"
#g=int(gHex,16)