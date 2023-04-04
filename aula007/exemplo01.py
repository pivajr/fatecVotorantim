soma = 0
n = 0
for x in range(1,11):
    idade = int(input(f"Digite a {x}a. idade: "))
    if x == 5:
        continue
    soma = soma + idade
    n = n + 1
       

print(x)
print(n)
media = soma / n
print(f"A média das idades é igual a {media:.2f}")