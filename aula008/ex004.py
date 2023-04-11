frase = input("Digite a frase: ")
qtd = 0
for letra in frase:
    if letra.lower() == 'a':
        qtd += 1
    if letra.lower() == 'e':
        qtd += 1
    if letra.lower() == 'i':
        qtd += 1
    if letra.lower() == 'o':
        qtd += 1
    if letra.lower() == 'u':
        qtd += 1
print(f"Quantidade de vogais = {qtd}")