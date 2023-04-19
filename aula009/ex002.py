lista = []
for i in range(5):
    x = int(input(f"Digite o {i+1}o número: "))
    lista.append(x)

maior = max(lista)
posicao = lista.index(maior)

print(f'O maior numero é {maior} e sua posição é {posicao}.')
