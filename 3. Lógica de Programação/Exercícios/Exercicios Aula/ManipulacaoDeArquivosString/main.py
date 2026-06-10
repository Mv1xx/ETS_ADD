dic = {}
geral = []

with open("cat_breeds.csv", 'r', encoding='utf-8') as arquivo:
    for linha in arquivo.readlines():
        geral.append(linha.strip().split(";"))  # tira o \n


print()
print()
print()
print()

# Cabeçalhos estão na primeira linha
cabecalhos = geral[0]
# Primeira linha de dados (por exemplo)

indice_1 = 0
indice_2 = 1
for chave in cabecalhos:
    valores = geral[indice_2]
    dic[chave] = valores[indice_1]
    indice_1 += 1
    indice_2 += 1

print(dic)
