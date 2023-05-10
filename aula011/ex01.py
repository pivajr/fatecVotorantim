lista = []
for i in range(5):
    x = int(input("Digite um valor: "))
    lista.append(x)
# converte a lista em uma tupla
t = tuple(lista)
# mostra a tupla na ordem inversa
print(t[::-1])
