
while True:
    try:
        print("1. Soma\n2. Subtração\n3. Divisão\n4. Multiplicação\n5. Sair")
        opcao = int(input("Escolha uma opção: "))
        n1 = float(input("Digite um numero: "))
        n2 = float(input("Digite outro número: "))
        break
    except ValueError:
        print('-=' * 20)
        print("Erro. Digite um valor válido!")

try:
    match opcao:
        case 1:
            calculo = n1 + n2
            print(f"{n1} + {n2} = {calculo}")
        case 2:
            calculo = n1 - n2
            print(f"{n1} - {n2} = {calculo}")
        case 3:
            calculo = n1 / n2
            print(f"{n1} / {n2} = {calculo}")
        case 4:
            calculo = n1 * n2
            print(f"{n1} * {n2} = {calculo}")
        case 5:
            print("Programa Finalizado")
        case _:
            print("Digite uma opção válida!")
            
except ZeroDivisionError:
    print('-=' * 20)
    print("Erro!")
            
