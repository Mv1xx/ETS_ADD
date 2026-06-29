from typing import List

def iterate(matriz : List[List[int]]) -> None:
    resultado = list()
    quadrante2 = list()
    quadrante3 = list()
    quadrante4 = list()
    
    
    for quadrante in range(4):
        for linha in range(0, 5, 1):
            for coluna in range(0, 5, 1):
                #resultado.append(matriz[linha][coluna])
                
                match quadrante:
                    case 2:
                        #matriz[linha][9 - coluna]
                        quadrante2.append(matriz[linha][9 - coluna])
                    case 3:
                        #matriz[9 - linha][coluna]
                        quadrante3.append(matriz[9 - linha][coluna])
                    case 4:
                        #matriz[9 - linha][9 - coluna]
                        quadrante4.append(matriz[9 - linha][9 - coluna])
                        
    resultado.append(matriz[linha][coluna])
    resultado.append(quadrante2)
    resultado.append(quadrante3)
    resultado.append(quadrante4)
    print(resultado)
                        
                
                


test_result : List[List[int]] = [
    [1,  2,  3,  4,  5,    5,  4,  3,  2,  1 ],
    [6,  7,  8,  9,  10,   10,  9,  8,  7,  6 ],
    [11, 12, 13, 14, 15,   15, 14, 13, 12, 11 ],
    [16, 17, 18, 19, 20,   20, 19, 18, 17, 16 ],
    [21, 22, 23, 24, 25,   25, 24, 23, 22, 21 ],

    [21, 22, 23, 24, 25,   25, 24, 23, 22, 21 ],
    [16, 17, 18, 19, 20,   20, 19, 18, 17, 16 ],
    [11, 12, 13, 14, 15,   15, 14, 13, 12, 11 ],
    [6,  7,  8,  9,  10,   10,  9,  8,  7,  6 ],
    [1,  2,  3,  4,  5,    5,  4,  3,  2,  1 ]
]   
                       
develop : List[List[int]] = [                
    [6,  73, 29, 12, 32,   100, 39, 18, 67, 85],
    [70, 20, 59, 4,  28,   43,  3,  60, 93, 84],
    [95, 40, 2,  99, 33,   52,  47, 21, 30, 23],
    [17, 71, 35, 10, 61,   91,  92, 42, 98, 13],
    [57, 26, 22, 7,  14,   11,  55, 25, 41, 76],
                           
    [27, 16, 45, 63, 15,   50,  72, 66, 31, 65],
    [89, 75, 48, 94, 1,    19,  80, 53, 36, 58],
    [24, 83, 34, 62, 78,   5,   9,  97, 82, 96],
    [38, 88, 8,  68, 74,   79,  46, 37, 64, 49],
    [87, 90, 44, 51, 86,   77,  56, 69, 81, 54]
]

result : None = iterate(test_result)
print(result)