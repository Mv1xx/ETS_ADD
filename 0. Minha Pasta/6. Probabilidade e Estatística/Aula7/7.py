import formulas

afirmacao = 12
amostra = 64
media = 11
desvio_padrao = 4
z = 1.96
a=0.05

resultado_confianca = formulas.intevalo_confianca(z, desvio_padrao, amostra, media)
print("Intervalo de confiança: ", resultado_confianca)

h = 12
hipotese_12 = formulas.Z(media, h, amostra, desvio_padrao)
print("Hipotese como media = 12: ", hipotese_12)
tabela = 0.0228

if tabela <= a:
    print("Rejeita!")
else:
    print("Nao rejeita!")