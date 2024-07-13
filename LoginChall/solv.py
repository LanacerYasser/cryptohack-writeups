#you should visit the README.md file before reading this code


ct = 'IVBYVA ERTVBA ONFR HCCRE'
flag = ''
key = 1

for key in range(1,26):
    for c in ct :
        if c != ' ':
            x = ord(c)
            D_x = (x - key)
            if D_x < ord('A'):
                D_x += 26
            flag += chr(D_x)
        else :
            flag += ' '
    print(flag)
    flag = ''

