import json
import numpy as np
import pandas as pd

nova_estrutura = {'id_pedido': 0, 'nome_cliente': '', 'valor_total': 0}

with open ('pedidos.json', 'r') as pedidos:
    a = json.load(pedidos)

