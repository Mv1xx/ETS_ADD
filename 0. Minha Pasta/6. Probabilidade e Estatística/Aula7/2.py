import formulas
#Teste de hipotese para média

amostra = 36
media = 6.5
desvio_padrao = 1.8
afirmacao = 7
a = 0.05

resultado = formulas.Z(media, afirmacao, amostra, desvio_padrao)
print(resultado)

tabela = 0.0475

if tabela <= a:
    print("Rejeita!")
else:
    print("Não Rejeita!")



