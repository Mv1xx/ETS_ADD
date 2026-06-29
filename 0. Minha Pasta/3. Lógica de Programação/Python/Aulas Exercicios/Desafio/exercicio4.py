cadastro = {}

while True:
    nome = str(input("Digite o nome: "))
    hobby = str(input("Digite o hobby: "))
    cadastro[nome] = hobby
    #nome : hobby | maria : joga
    
    continuar = input("Deseja cadastrar outro usuário? (s/n) ").lower()

    while continuar not in ['s', 'n']:
        print("Digite um valor válido. Tente novamente! ")
        continuar = input("Deseja cadastrar outro usuário? (s/n) ").lower()
    
    if continuar == 'n':
        break

#exibindo informações cadastradas
print('\n')
for i in cadastro:
    print(f"Nome: {i}")
    print(f"Hobby: {cadastro[i]}")
    print('\n')