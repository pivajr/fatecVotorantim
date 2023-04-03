idade = int(input("Entre com sua idade: "))
if (idade >= 5) and (idade <= 7):
    print("Categoria: INFANTIL")
elif (idade >= 8) and (idade <= 10):
    print("Categoria: JUVENIL")
elif (idade >= 11) and (idade <= 15):
    print("Categoria: ADOLESCENTE")
elif (idade >= 16) and (idade <= 30):
    print("Categoria: ADULTO")
elif (idade > 30):
    print("Categoria: SÊNIOR")
else:
    print("Idade inválida!!")