import pandas

def fazendo_login():
    print('1. Aluno\n2. Professor\n3. Direção')
    usuario = int(input("\nUsuário:\n>> "))

    #usuario inválido
    while usuario not in [1, 2, 3]:
        print("Digite um usuário válido!")
        usuario = int(input("Usuário:\n>> "))

    usuario = tipo_usuario(usuario)
    num_matricula = input("\nNúmero de matrícula:\n>> ")
    senha = input("\nSenha:\n>>")

    logado = validando_login(cadastros, usuario, num_matricula, senha)

    return logado

def validando_login(cadastros, usuario, num_matricula, senha):
    login = False
    for user in cadastros:
        dados = cadastros[user]

        if usuario == user:
            for matricula in dados:
                infos = dados[matricula]
                if num_matricula == matricula and infos[1] == senha:
                    login = True
                
    return num_matricula, usuario, senha, login
                    
def tipo_usuario(usuario):
    match usuario:
        case 1:
            return 'alunos'
        case 2:
            return 'professores'
        case 3:
            return 'direcao'

cadastros = {
            'alunos' : { '000123' :  ['Maria', '123'], '000456' : ['João', '456']},
            'professores' : { '000789' : ['Adriana', '789']}, 
            'direcao' : { '000101' : ['Edineia', '101']}
            }

cadastro = pandas.read_csv("Cadastros.csv", encoding="utf-8")

print('----- BEM-VINDO -----\n')

num_matricula, usuario, senha, logado = fazendo_login()

# if login == True:
#     match usuario:
#         case 1:
#             nota_aluno()
#         case 2:
#             nota_turma()
#             nota_aluno()
#         case 3:
#             nota_aluno()
#             nota_turma()
#             cadastrar_user()
#             remover_user()
# else:

#se informações não estiverem corretas...
while logado == False:
    print("\n!!! informações inválidas!, Tente Novamente !!!\n")
    num_matricula, usuario, senha, logado = fazendo_login()

print(logado)

        