# CuliArts - ElBeyet

![](https://github.com/nourmami/CTF-Writeups/blob/writeup/Securinets_Esprit_CTFLeague/CuliArts/Elbeyet/elbeyet.png)

## IV Recovering
### Imaging having the IV,key and the ciphertext of your flag with AES-CBC mode. You've probably already guessed it, what's left is to apply the decryption function to these 3 parameters.And recover the flag.
In this challenge we already know that:
```python 
    Key = IV
```
and the ciphertext of our flag (encrypted-flag)
```python 
    enc_flag = encrypt(FLAG)
    print("\n\nThis is a very old meal, I cannot recognize its taste anymore:", enc_flag)
```

### Also we have a decryption Oracle. Unfortunatly, :( we can't bypass the encrypted-flag due to the `check-leak` function :
```python 
   def check_leak(msg):
	msg_blocks = [msg[i: i+BLOCK_SIZE] for i in range(0, len(msg), BLOCK_SIZE)]
	flag_blocks = [FLAG[i: i+BLOCK_SIZE] for i in range(0, len(FLAG), BLOCK_SIZE)]
	for msg_block in msg_blocks:
		for flag_block in flag_blocks:
			if msg_block == flag_block:
				return True
	return False
```
### happely we can recover the IV, as already mentioned before.
to do so let's review the decryption AES-CBC process:

![](https://miro.medium.com/max/1400/1*4gWh_cwfK4Sr_aRaodqKLQ.png)

Imagine having 2 blocks of ciphers `c1` and `c2` as shown:
|           | ciphetext | plaintext |
| --------- | --------- | --------- |
| Block1    | C1 | P1 |
| Block2    | C2 | P2 |

### We can then write
```python 
    P1=IV ^AES(key,C1)
    P2=C1 ^AES(key,C2)
```
### What if we choose C1=C2, we'll certainly have:
```python 
    AES_Decrypt(key,C1)==AES_Decrypt(key,C2)
```
### Xoring the two equations we'll get:
```python 
    IV^C1^AES_Decrypt(key,C1)^AES_Decrypt(key,C1)==P1^P2
    IV^C1==P1^P2
```
> A `XOR` A=0 
### To make things easier  let's take:
```python 
    C1==C2==0000000000000000
    IV==P1^P2
```
> A `XOR` 0=A

### And that's it here you have your iv,key and cipher so let's jammer (decrypt) it. check `elbeyetSover.py`
