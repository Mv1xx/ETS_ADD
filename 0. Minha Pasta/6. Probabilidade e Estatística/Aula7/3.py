import formulas
import math
#teste de hipotese para probabilidade

afirmacao = 55
amostra = 400
media = 220
a = 0.05

#Defina as hipoteses
#H0 <= 0,55
#H1 > 0,55

#Realize o teste de proporcao
resultados = formulas.proporcao(media, 0.55, 0.45, amostra)
print(resultados)

tabela = 0.500

if tabela <= a:
    print("Rejeita!")
else:
    print("Não Rejeita!")
