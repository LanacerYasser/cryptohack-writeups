#you should read the README file before reading this

def xor(bytes1,bytes2) :
    return  bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])


ct = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
flag_format = b'crypto{XXX}'


key = xor(flag_format[:7],ct[:7]) 

key = key + b'y'

flag = b''

for i in range(0,len(ct),8) :
    flag += xor(key,ct[i:i+8])

print(flag)
