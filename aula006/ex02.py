valor_compra = float(input("Valor da compra: "))
if valor_compra > 5000:
    desconto = valor_compra * 0.3
else:
    if valor_compra <= 1000:
        desconto = valor_compra * 0.1
    else:
        desconto = valor_compra * 0.2
novo_valor = valor_compra - desconto
print(f"Valor da Compra: {valor_compra:10.2f}")
print(f"Valor  Desconto: {desconto:10.2f}")
print(f"Novo Valor.....: {novo_valor:10.2f}")