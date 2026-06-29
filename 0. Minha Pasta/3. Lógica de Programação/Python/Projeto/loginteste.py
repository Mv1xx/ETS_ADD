import pandas
# def validando_login(cadastros, usuario, num_matricula, senha):
#     login = False

#     for user in cadastros:
#         dados = cadastros[user]

#         if usuario == user:
#             for matricula in dados:
#                 infos = dados[matricula]
#                 if num_matricula == matricula and infos[1] == senha:
#                     login = True
                
#     return num_matricula, usuario, senha, login
                    
# num_matricula = '000101'
# senha = '101'
# usuario = 'aluno'

cadastros = pandas.read_csv("Cadastros.csv", encoding="utf-8", sep=';')
print(cadastros['Senha'].astype(int))

# for i in range(len(cadastros)):
#     print(cadastros['Senha'][i])
#     if cadastros['Senha'][i] == 101:
#         print(cadastros['Senha'][i])
#percorrer a coluna de cargo, numero de matricula e senha
