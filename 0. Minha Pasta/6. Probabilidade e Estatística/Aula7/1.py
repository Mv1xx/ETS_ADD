import formulas


amostra = 64
media = 9.4
desvio_padrao = 2.4
a = 1.96 #95%

resultado = formulas.intevalo_confianca(a, desvio_padrao, amostra, media)
print(resultado)
