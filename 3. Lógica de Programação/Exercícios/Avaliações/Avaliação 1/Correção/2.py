import random as rd

s = rd.randint(1,1000)
c = None
count = 0
print(s)
while s != c:
    c = int(input('Chuta ai:\n>> '))
    count += 1
    if 0 < abs(c-s) <= 3:
        print('esta perto...')
    elif c > s:
        print('menor!')
    elif c < s:
        print('maior!')

print('Parabens! Numero de tentativas: ', count)