idades = {
    'ana': 34,
    'pedro': 31,
    'josé': 45,
    'joão': 18
}
soma = 0
for idade in idades.values():
    print("A idade que está sendo somada agora é ", idade)
    soma += idade

media = soma / len(idades)

print(f"A média das idades é {media}")