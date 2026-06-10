def criptografar_cesar(texto:str, deslocamento:int):
    lista_cripto = []
    
    for char in texto:
        novo_char = chr((ord(char) + deslocamento - ord('a')) % 26 + ord('a'))
        lista_cripto.append(novo_char)
    
    texto = ''.join(lista_cripto)
    
    return texto

def descriptografar_cesar(texto:str, deslocamento:int):
    lista_cripto = []
    
    for char in texto:
        novo_char = chr((ord(char) - deslocamento - ord('a')) % 26 + ord('a'))
        lista_cripto.append(novo_char)
    
    texto = ''.join(lista_cripto)
    
    return texto

texto = input("Digite o texto desejado: ").lower()
deslocamento = int(input("Digite a quantidade de casas no alfabeto que deseja deslocar: "))

texto = criptografar_cesar(texto, deslocamento)
print(texto)
texto = descriptografar_cesar(texto, deslocamento)
print(texto)