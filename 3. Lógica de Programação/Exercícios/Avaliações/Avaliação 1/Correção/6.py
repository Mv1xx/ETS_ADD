import random as rd

matrix = []
lines = int(input('linhas:\n>> '))
columns = int(input('colunas:\n>> '))

print('\n\n')
for i in range(lines):
    line = []
    for j in range(columns):
        line.append(rd.randint(0,9))
    matrix.append(line)


sum_par = 0
for line in matrix:
    for element in line:
        print(element, end='\t')
        if element % 2 == 0:
            sum_par += element
    print('\n')

print('soma dos numeros pares: ', sum_par)