lista = []
for i in range(5):
    x = int(input(f"Digite o {i+1}o número: "))
    lista.append(x)

print(lista)
print(lista[::-1])
