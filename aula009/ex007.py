numeros = [0]*10
indice = 0
qtd = 0
x = 101
while qtd < 10:
    primo = False
    div = 0
    for i in range(1, x):
        if (x % i) == 0:
            div = div + 1
    if div == 1:
        primo = True
    if primo:
        numeros[indice] = x
        indice = indice + 1
        qtd = qtd + 1
    x = x + 1
print(numeros)