l1 = []
l2 = []
for i in range(5):
    x = int(input(f"L1 - Digite o {i+1}o. valor: "))
    l1.append(x)
print("L1 = ", l1)
for i in range(5):
    x = int(input(f"L2 - Digite o {i+1}o. valor: "))
    l2.append(x)
print("L2 = ", l2)
#transforma as listas em conjuntos
c1 = set(l1)
c2 = set(l2)
print("C1 = ", c1)
print("C2 = ", c2)
# une as duas listas
c = c1.union(c2)
# mostra o conjunto final
print(c)