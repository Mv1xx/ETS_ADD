import json
import time
import os

if os.path.isdir("dados") == False:
    os.mkdir("dados")

# print(os.path.isfile("./dados/tarefas.json"))

with open('./dados/tarefas.json', 'r', encoding='utf-8') as tarefas:
    t = json.load(tarefas)

# print(t)

nova_tarefa = {"nome" : "Estudas Python", 'criado_em' : 17000000}




