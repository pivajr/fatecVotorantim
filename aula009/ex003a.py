vet1 = []
vet2 = []
vet3 = []
for i in range(3):
    x = int(input(f"Digite o {i+1}o valor (vet1):  "))
    vet1.append(x)
for i in range(3):
    x = int(input(f"Digite o {i+1}o valor (vet2):  "))
    vet2.append(x)

for i in range(3):
    vet3.append(vet1[i])
    vet3.append(vet2[i])

print(vet3)