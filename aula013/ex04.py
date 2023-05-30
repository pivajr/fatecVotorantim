from random import randint
def geralista():
    lista = []
    for i in range(10):
        lista.append(randint(1,1000))
    return lista
#Script
l = geralista()
print("Lista: ", l)
print(f"Maior Valor = {max(l)}")
print(f"Menor Valor = {min(l)}")
print(f"Valor Médio = {sum(l)/len(l)}")



