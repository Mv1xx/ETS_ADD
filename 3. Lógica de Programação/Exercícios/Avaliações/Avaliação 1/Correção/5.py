cad = True

alunos = []
while cad:
    s = input('0 - sair | Qualquer - continuar')
    if s == '0':
        break
    
    nome = input('nome: ')

    idade = int(input('idade: '))
    matematica = int(input('nota em matematica: '))
    portugues = int(input('nota em portugues: '))
    ciencias = int(input('nota em ciencias: '))
    notas = (matematica, portugues, ciencias)

    aluno = {'nome' : nome, 'notas' : notas}
    alunos.append(aluno)

print('Relatório:')
for aluno in alunos:
    media = sum(aluno['notas']) / 3
    media = round(media, 2)
    print(f'Nome: {aluno['nome']}\t| Média: {media}')