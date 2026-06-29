import random

simulacao = 1000
lancamento = 100
moeda = ["cara", "coroa"]
cont = 0
justa = True

for i in range(simulacao):
    qnt_cara = 0
    for j in range(lancamento):
        chance = random.choice(moeda)
        if chance == "cara":
            qnt_cara += 1
    if qnt_cara >= 65:
        cont += 1
        justa = False

print(f"Frequencia q cara saiu += 65 vezes: ", cont)
if justa == True:
    print("Moeda Justa!")
else:
    print("Moeda Injusta!")