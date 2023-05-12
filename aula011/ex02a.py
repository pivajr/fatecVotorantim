dic = {}
for i in range(5):
    nome = input(f"Entre com o {i+1}o. nome: ")
    idade = int(input(f"Entre com a {i+1}a. idade: "))
    dic[nome] = idade
soma = 0
for idade in dic.values():
    soma += idade
media = soma / len(dic)
print(f"A média das idades é {media}")

for nome, idade in dic.items():
    if idade > media:
        print(f"{nome} tem {idade} anos!")
