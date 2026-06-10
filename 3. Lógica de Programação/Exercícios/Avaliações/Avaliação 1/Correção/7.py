p = input('frase:\n>> ')                # Recebe a frase a ser criptografada
n = int(input('passo:\n>> '))           # O passo usado para criptografar


def funcao(frase, passo):               # Função que criptografa
    secreto = []                        # Variável que vai guardar a nossa frase após ser criptografada
    for letra in frase:                 # Looping para percorrer a frase original
        letra_secreta = chr(
            (
                ord(letra) - ord('a') + passo # subtraimos o valor da tabela ascii da 
            ) % 26 + ord('a'))                # letra 'a' do valor da letra escondida 
                                              # para obter a distancia de 'a', e então fazemos 
                                              # módulo de 26 pois são 26 letras do alfabeto,
                                              # assim conseguimos a posição da nossa letra
                                              # em relação ao alfabeto, somamos o passo para esconder
                                              # e então devolvemos o valor de 'a' para manter
                                              # a conformidade com a tabela ascii 
            
        secreto.append(letra_secreta)

    return ''.join(secreto)

print(funcao(p,n)) 