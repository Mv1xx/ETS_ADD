import random

class ApostaErro(Exception):
    pass

#valores cartas
cartas = {'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 1, 
          '2' : 2, '3' : 3, '4': 4, '5' : 5,
          '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10}

#lista com as chaves do dicionário 'cartas'
chaves = list(cartas.keys())
valor_jogador = list()
valor_bot = list()

#criando erro de aposta inválida
def verifica_aposta(apo):
    if 10 > apo or apo > 500:
        raise ApostaErro()
    print("Aposta Feita!")

while True:
    try:
        aposta = int(input("Escolha um valor para apostar até 500: "))
        verifica_aposta(aposta)
        break
    except ApostaErro:
        print("!!!Digite um valor válido!!!\n")

#verificando se escolha é um valor válido
def escolha_funcao(e):
    while e not in [1, 2]:
        print("Opção inválida, tente novamente.")
        escolha = int(input("Escolha uma opção: "))
    return e

#sorteando uma carta (hit)
def hit_funcao():
    cartas_hit = random.choice(chaves)
    return cartas_hit

#calculando valores das cartas jogador
def calcula_cartasj(cj):
    valor_jogador.clear()
    for valores in cj:
        valor_jogador.append(cartas[valores])
    return valor_jogador

#calculando valores das cartas bot
def calcula_cartasb(cb):
    valor_bot.clear()
    for valores in cb:
        valor_bot.append(cartas[valores])
    return valor_bot

def verificando_ganhador(tj, tb):
    if min(tj, tb) == tb:
        return "Parabens, Você Ganhou!!"
    else:
        return "AAAHH, que pena :( você perdeu.\nBoa Sorte na próxima vez"
        
#sorteando cartaspara iniciar jogo
cartas_jogador = random.sample(chaves, 2)
cartas_bot = random.sample(chaves, 2)
print(cartas_jogador)

#definindo valores totais para iniciar
total_bot = 0
total_jogador = 0

#enquanto ninguem ganhar...
while True:
    #soma valores das cartas do jogador
    total_jogador = sum(calcula_cartasj(cartas_jogador))
    print(f"O seu total é: {total_jogador}")
    print('-=' * 15)
    
    #soma valores das cartas do bot
    total_bot = sum(calcula_cartasb(cartas_bot))
    
    if total_jogador >= 21 or total_bot >= 21:
        break
    
    #escolha uma opção
    print("1. HIT!!!\n2. Parar")
    escolha = int(input("Escolha uma opção: "))
    print('-=' * 15)
    
    if escolha_funcao(escolha) == 2:
        break
    elif escolha_funcao(escolha) == 1:
        cartas_jogador.append(hit_funcao())
        print(cartas_jogador)
  
print(verificando_ganhador(total_jogador, total_bot))
print("Jogo finalizado!")
print(f"Seu total: {total_jogador}")
print(f"Total do bot: {total_bot}")







    






