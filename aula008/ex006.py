frase = input("Digite a frase: ").upper()
print(frase)
frase_limpa = frase.replace(" ", "")
print(frase_limpa)
frase_invertida = frase_limpa[::-1]
print(frase_invertida)
if frase_limpa == frase_invertida:
    print("A frase é palindroma!")
else:
    print("A frase NÃO é palindroma!!")