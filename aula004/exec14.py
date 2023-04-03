valor = float(input("Entre com o valor: "))
hora = int(valor)
minutos = (valor - hora) * 100
total_minutos = hora * 60 + minutos
print(f"Total de minutos: {total_minutos}")