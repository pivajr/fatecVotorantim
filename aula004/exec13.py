salario_minimo = float(input("Entre com o SM R$ "))
kilowatts = int(input("Digite o total de kwatts: "))
valor_kw = salario_minimo / 80
conta = valor_kw * kilowatts
conta_desconto = conta - (conta * 0.15)
print(f"Valor Kilowatts...: R$ {valor_kw:.2f}")
print(f"Conta de Energia..: R$ {conta:.2f}")
print(f"Conta com Desconto: R$ {conta_desconto:.2f}")