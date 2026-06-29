import formulas

afirmacao = 30
amostra = 49
media = 31
desvio_padrao = 7
a = 0.01

resultado = formulas.Z(media, afirmacao, amostra, desvio_padrao)
print(resultado)

tabela = 0.8913

if tabela <= a:
    print("Rejeita!")
else:
    print("Não rejeita!")