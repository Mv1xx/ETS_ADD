

frase = input("Digite uma frase: ")

if frase.isnum():
    print("aaaaa")
else:
    print("bbbbb")

frase = frase.replace(" ", "").lower()
frase = list(frase)

frase_invertida = list(reversed(frase))

print(frase)
print(frase_invertida)

if frase == frase_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")


