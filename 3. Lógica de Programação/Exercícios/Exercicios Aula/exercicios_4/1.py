a = None
option = None
operations = ['+', '/', '*', '-']
while option != '=':
    b = None
    while a == None or type(a) != int:
        try:
            a = int(input('Digite o primeiro número >>  '))
        except(ValueError):
            print('Voce deve inserir um número válido!')

    option = input(f'Digite a operação desejada {operations} >>  ')
    if option == '=':
        break
    if not option in operations:
        raise ValueError('Operação não encontrada!')

    while type(b) != int:
        try:
            b = int(input('Digite o próximo número >>  '))
        except:
            print('Voce deve inserir um número válido!')

    match option:
        case '+':
            a = a + b
        case '-':
            a = a - b
        case '/':
            a = a / b
        case '*':
            a = a * b
print(a)
    