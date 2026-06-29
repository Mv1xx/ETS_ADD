import os
#para que esse exercicio funcione corretamente, somente a pasta Exercicios deve ser aberta na IDE. 
# Caso contrário, a função listdir não irá listar todos os arquivos que queremos!!!!!!!!!

caminho_atual = os.path.abspath('')
print(caminho_atual)
count = 0

pasta_pdf = os.path.join(caminho_atual, 'PDF')

if os.path.isdir(pasta_pdf) == False:
    arquivos = os.listdir()
    os.mkdir("PDF")
    pasta_pdf = os.path.join(caminho_atual, 'PDF')

    for i in arquivos:
        nome, tipo = i.split(".")
        print(nome, tipo)
        
        if tipo == 'pdf':
            count += 1
            caminho_arquivo_antigo = os.path.join(caminho_atual, i)
            caminho_arquivo_novo = os.path.join(pasta_pdf, i)
            os.rename(caminho_arquivo_antigo, caminho_arquivo_novo)

print(f"{count} arquivos PDF movidos para a pasta 'PDF'")

