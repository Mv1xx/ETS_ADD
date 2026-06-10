import random as rd
from lib import get_data
from typing import List, Tuple, Dict, Any

def filter(dados : List[Dict[str,str]], colunas_comparacao : Dict[str, List[str]]) -> None:
    pass
            


def map(dados : List[Dict[str, Any]], colunas_modificacao : Dict[str, str]) -> None:
    pass
def group(dados : List[Dict[str,str]], colunas_reduzidas : List[str]) -> None:
    pass


dados : List[Dict[str, str]] = get_data('./gatos.csv', ';')
rd.shuffle(dados)
