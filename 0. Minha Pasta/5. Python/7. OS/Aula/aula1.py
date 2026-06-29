import os

#lista as pastas e arquivos de um caminho
print(os.listdir())

#criar um novo diretório - PASTA
os.mkdir("nome_pasta")

#verificar se um arquivo existe dentro de uma pasta | True or False
os.path.isfile("caminho")

#verifica se há uma pasta | True or False
os.path.isdir("caminho")

#junta duas strings q resulta em um caminho 
novo_local = os.path.join("nome_pasta", "arquivo")


os.rename("arquivo", novo_local) #renomeia o caminho do arquivo - recorta de lugar



