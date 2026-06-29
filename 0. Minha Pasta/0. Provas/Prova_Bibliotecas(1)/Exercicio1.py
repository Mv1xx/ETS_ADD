import numpy as np

temperaturas = np.random.randint(18, 40, 28).reshape((4,7))

print(temperaturas)

#propriedades da matriz
print(temperaturas.ndim)
print(temperaturas.shape)

#c
temperaturas_copia = temperaturas.reshape((7,4))
print(" ")
print(temperaturas_copia)

#d
temperaturas_corrigidas = temperaturas + 1.5
print(" ")
print(temperaturas_corrigidas)

#e
print("----------------------")
print(temperaturas)
media_maquina = temperaturas.mean(axis=0)
media_dia = temperaturas.mean(axis=1)

print("Média por máquina: ", media_maquina.mean())
print("Média por dia: ", media_dia.mean())

# print("Média de temperatura por máquina: ", round(media_maquina.mean(), 2))
# print("Média de temperatura por dia: ", round(media_dia.mean(), 2))


#f
print(" ")
print("Temperatura Máquina 1: ", temperaturas_corrigidas[0, 1])
print("Temperaturas registradas no dia 5: ", temperaturas_corrigidas[:, 4])
print("Temperaturas das máquinas 1, 3 nos primeiros 4 dias: \n", temperaturas_corrigidas[:3, :5])

print("\nTemperaturas maiores que 35 graus: ", temperaturas_corrigidas[temperaturas_corrigidas > 35])

menos22 = temperaturas_corrigidas[temperaturas_corrigidas < 22]

print("menos 22 graus: ", menos22)

print("média geral: ", temperaturas_corrigidas.mean())
print("valor máximo: ", temperaturas_corrigidas.max())
print("Valor mínimo: ", temperaturas_corrigidas.min())
print("desvio padrão: ", temperaturas_corrigidas.std())



