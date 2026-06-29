import os

pasta = os.getcwd() #--> OS

for arquivo in os.listdir(pasta):
    att = arquivo
    a, b = arquivo.split(".")
    os.mkdir(f"Pasta {b}")
    novo_caminho = os.path.join(pasta, f"Pasta {b}/{att}")
    os.rename(att, novo_caminho)



