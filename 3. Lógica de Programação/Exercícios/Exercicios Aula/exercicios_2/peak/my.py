'''
=============================================
Desenvolva uma maneira de encontrar onde 
está o maior valor da matriz.

Exiba o indice de linha e coluna onde o
maior valor se encontra
=============================================
'''

from peak_lib import gen_peak

lines = 10
columns = 10

montanha = gen_peak(lines,columns,100)

for a in montanha:
    print(*a)



def a(array, start = 0, end = None):
    
    length = len(array)

    if end == None:
        end = length

    if length == 1:
        return array[0]

    search_line_idx = int(length/2) + 1 if length%2 == 0 else 0
    
    print(start, end)

    max_top = max(array[start:search_line_idx])
    max_down = max(array[search_line_idx:end])
    
    if max_top > max_down:
        return a(array, start, search_line_idx)
    else:
        return a(array, search_line_idx, search_line_idx+(search_line_idx-start))

array = [montanha[i][0] for i in range(lines)]

print(a(array))
