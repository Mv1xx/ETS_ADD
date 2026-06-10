digitos_string = input('digitos:\n>> ')

digitos_int = 0
for i in range(len(digitos_string)):
    digitos_int += (10**(len(digitos_string)-1-i))      * (ord(digitos_string[i])-48)

print(type(digitos_string))
print(digitos_string)
print(type(digitos_int))
print(digitos_int)
