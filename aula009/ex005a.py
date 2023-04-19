from random import randint
sorteio = [0]*7
perc = [0]*7
for i in range(6000):
    x = randint(1,6)
    sorteio[x] = sorteio[x] + 1

for j in range(1, 7):
    perc[j] = sorteio[j] / 6000

for j in range(1, 7):
    print(f"O lado {j} foi sorteado {sorteio[j]} - {perc[j]:.2%}")

