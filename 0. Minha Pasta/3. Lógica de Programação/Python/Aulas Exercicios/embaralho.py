import random

palavras = ['banguela', 'dente-de-anzol', 'tempestade', 'batatão', 'vomito', 'Arroto', 'quebra-miólos']

palavra = random.choice(palavras)
lista_palavra = list(palavra)

random.shuffle(lista_palavra)

palavra_embaralhada = "".join(lista_palavra)

print(palavra_embaralhada)

advinha = input("Tente adivinha a palavra: ").lower()

while advinha != lista_palavra:
    print("Beep, errado, tente novamente")
    advinha = input("Tente adivinha a palavra: ").lower()