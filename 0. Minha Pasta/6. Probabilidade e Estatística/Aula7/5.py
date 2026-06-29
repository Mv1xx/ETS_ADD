import formulas

amostra = 150
media = 110
a = 0.05
afirmacao = 80

#h0 >= 80%
#h1 < 80%

resultado = formulas.proporcao(media, 0.8, 0.2, amostra)
print(resultado)

tabela = 0.0207

if tabela <= a:
    print("Rejeita!")
else:
    print("Não rejeita!")