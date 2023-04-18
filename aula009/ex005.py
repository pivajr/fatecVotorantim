from random import randint
dado = [0]*7
est = [0]*7
for i in range(6000):
    x = randint(1, 6)
    dado[x] = dado[x] + 1
for i in range(1, 7):
    est[i] = dado[i] / 6000
for i in range(1, 7):
    print(f'Lado {i} foi sorteado {dado[i]} = {est[i]:.2%}')



