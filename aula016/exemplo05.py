try:
    num = int(input("informe um número: "))
except:
    print("Valor incorreto!")
else:
    print(f"Você digitou {num}")
finally:
    print("Fim do Bloco")

