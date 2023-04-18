vet1 = [0]*3
vet2 = [0]*3
vet3 = []
for i in range(3):
    vet1[i] = int(input(f"Digite o {i+1}o valor (vet1):  "))
for i in range(3):
    vet2[i] = int(input(f"Digite o {i+1}o valor (vet2):  "))

for i in range(3):
    vet3.append(vet1[i])
    vet3.append(vet2[i])

print(vet3)