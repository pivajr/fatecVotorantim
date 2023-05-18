def eprimo(n):
    i = 1
    contador = 0
    while i <= n:
        if (n % i) == 0:
            contador += 1
        i += 1
    if contador == 2:
        return True
    else:
        return False

print("Os primeiros 50 números primos são os seguintes: ")
i, n = 2, 0
coluna = 1
while n <= 50:
    if eprimo(i):
        print(i, end=" - ")
        n += 1
        coluna += 1
    i += 1
    if coluna > 15:
        print()
        coluna = 1



