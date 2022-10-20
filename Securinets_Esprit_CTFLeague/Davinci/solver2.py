msg ="DaVinci|rm=1"
msg1="DaVindi|rm=1"
#print(len(msg))
xor = ord('c') ^ ord('d')
xor1= 4^ord('3')
xor2=4^ord('7')
xor3=4^1 
        
cipher ='f62c3bbd62eba8727cc6936ae1bbd79371c71daadcb6c6ca6584b825230a866d'
        
print(cipher[32:])
cipher0=cipher[:10] + hex(int(cipher[10:12], 16) ^ xor)[2:] + cipher[12:]
cipher = cipher[:10] + hex(int(cipher[10:12], 16) ^ xor)[2:] + cipher[12:24]+hex(int(cipher[24:26], 16) ^ xor1)[2:]+hex(int(cipher[26:28], 16) ^ xor1)[2:]+hex(int(cipher[28:30], 16) ^ xor2)[2:]+hex(int(cipher[30:32], 16) ^ xor3)[2:]+cipher[32:]
#print(cipher0)


print(cipher)
