import numpy as np
import math 

def bi(n, k, p):
    return math.comb(n, k) * (p**k) * ((1-p)**(n-k))

n = 20
p = 0.2

a = bi(n, 20, p)
b = np.sum([bi(n, k, p) for k in range(9,n+1)])
c = math.floor((n+1) * p)

print(a)
print(b)
print(c)

