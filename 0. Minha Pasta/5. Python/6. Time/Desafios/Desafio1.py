import time

frase = "Katy Perry é legal."

print(f"Digite: \n{frase}\n")

enter = input("Digite ENTER para iniciar ")

contador = time.time()

digitado = input()

if digitado == frase:
    tempo = time.localtime(contador)

    tempo_total = tempo.tm.sec
    total_char = len(digitado)
    
