with open('./anotacoes.txt', 'w') as anotacoes:     # Sobreescreve no arquivo
    anotacoes.writelines(['Sobre\n','escrevendo\n'])

with open('./anotacoes.txt', 'a') as anotacoes:     # Adiciona ao final
    anotacoes.writelines(['Adicio\n','nando\n'])

with open('./anotacoes.txt', 'r') as anotacoes:     # Lê o arquivo
    anotacoes.readline()
    for line in anotacoes.readlines():
        print(line)