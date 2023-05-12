idades = {
    'ana': 34,
    'pedro': 31,
    'josé': 45,
    'joão': 18
}
maior = 0
nome_maior = ''
for nome in idades.keys():
    if len(nome) > maior:
        maior = len(nome)
        nome_maior = nome
print(f"O maior nome é {nome_maior} e sua"\
    f"idade é {idades.get(nome_maior)}")