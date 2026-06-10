import random as rd

n = 26
s = int((n*(n+1)) / 2)

pir = [rd.randint(1,100) for _ in range(s)]
for i in range(n):
    print(' '*(n-i+1), end='')
    for j in range(i+1):
        layer_sum = int((i*(i+1))/2)
        print(pir[layer_sum+j], end=' ')
    print()

path = []
ll = int(((n-2)*(n-1))/2)
for i in range(n-1):
    left = pir[(ll)+i]   +pir[(ll)+i+(n-1)]
    right = pir[(ll)+i]  +pir[(ll)+i+(n-1)+1]
    direction = int(right > left)
    best = right if direction else left
    path.append((direction, best))

for i in range(n-2,0,-1):
    b = []
    for j in range(i):
        ls = int(((i-1)*i)/2)

        left = pir[(ls)+j]   +path[len(path)-1-i+j][1]
        right = pir[(ls)+j]  +path[len(path)-i+j][1]

        direction = int(right > left)

        best = right if direction else left
        # print(
        #     'original: ', pir[(ls)+j],
        #     ' | left: ', path[len(path)-1-i+j][1], 
        #     ' | right: ', path[len(path)-i+j][1],
        #     ' | best: ', best
        # )
        b.append((direction, best))
    path.extend(b)
    # print('----')

for i in range(n-1):
    print(' '*(n-i+1), end='')
    for j in range(i+1):
        layer_sum = int((i*(i+1))/2)
        print(path[len(path)-1-layer_sum+j], end=' ')
    print()
