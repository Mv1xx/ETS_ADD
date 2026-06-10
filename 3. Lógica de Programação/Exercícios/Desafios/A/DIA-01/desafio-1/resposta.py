from lib import get_data
from typing import List, Dict

def is_connected(relations: Dict[str,List[str]] , a: str, b : str):
    caminho = [a]
    
    while (not b in caminho) and caminho != []:
        print(caminho)
        input()
        crr = caminho[-1]
        if relations[crr] == []:
            caminho.pop()
            continue
        caminho.append(relations[crr].pop(0))
    
    return b in caminho


entidades : Dict[str, List[str]]= get_data('./data.txt')
r = is_connected(entidades, '22', '16')
print(r)