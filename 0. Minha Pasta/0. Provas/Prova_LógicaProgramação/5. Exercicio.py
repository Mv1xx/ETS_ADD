
nome = input("Digite o nome do aluno (ou 'sair' para encerrar): "). capitalize()
mat = int(input("Nota de Matemática: "))
por = int(input("Nota de portugues: "))
cien = int(input("Nota de Ciências: "))

historico = {
             'Nycollas' : {'idade' : 14, 'Matemática' : (), 'Português' : (), 'Ciências' : ()},
             'Lorena' : {'idade' : 12, 'Matemática' : (), 'Português' : (), 'Ciências' : ()}
             }

for i in historico:
    if i == nome:
        for j in historico[i]:
           if j == 'Matemática':
               historico[i][j] = mat
               print("Nota de Matemática: ", historico[i][j])
               
            

            


