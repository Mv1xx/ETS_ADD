data = str(input("Digite uma data (dd/mm/aaaa): "))

dia, mes, ano = data.split('/')

match mes:
    case '01':
        print(f"{dia} de Janeiro de {ano}")
    case '02':
        print(f"{dia} de Fevereiro de {ano}")
    case '03':
        print(f"{dia} de Março de {ano}")
    case '04':
        print(f"{dia} de Abril de {ano}")
    case '05':
        print(f"{dia} de Maio de {ano}")
    case '06':
        print(f"{dia} de Junho de {ano}")
    case '07':
        print(f"{dia} de Julho de {ano}")
    case '08':
        print(f"{dia} de Agosto de {ano}")
    case '09':
        print(f"{dia} de Setembro de {ano}")
    case '10':
        print(f"{dia} de Outubro de {ano}")
    case '11':
        print(f"{dia} de Novembro de {ano}")
    case '12':
        print(f"{dia} de Dezembro de {ano}")
    case _:
        print("Mês Invalido!")