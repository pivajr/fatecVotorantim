idades = {
    'ana': 34,
    'pedro': 31,
    'josé': 45,
    'joão': 18
}
maior = ''
for nome in idades.keys():
    print("O nome visto é ", nome)
    if len(nome) > len(maior):
        maior = nome

print(f"O maior nome é {maior}")
      