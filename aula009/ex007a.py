x = int(input("Digite um número: "))
primo = False
qtd = 0
for i in range(1, x):
    if (x % i) == 0:
        qtd = qtd + 1
if qtd == 1:
    primo = True
if primo:
    print(f"O número {x} é primo!")
else:
    print(f"O número {x} não é primo!")