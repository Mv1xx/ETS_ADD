import json
import numpy as np
import pandas as pd

with open ('pedidos.json', 'r') as pedidos:
    a = json.load(pedidos)

print(a)