print('Comparativo de Consumo de Combustivel')
veiculos = []
consumo = []
preco = 2.25
for i in range(1, 6):
    veiculos.append(input(f'Veiculo {i}: '))
    consumo.append(float(input('Km por litro: ')))
print('Relatorio Final')
menorConsumo = 0
for i in range(0, 5):
    custo = 1000 / consumo[i]
    gasto = custo * preco
    print(f'{i+1} - {veiculos[i]:10} - {consumo[i]:6.2f} - {custo:6.1f} litros - R$ {gasto:6.2f}')
    if (consumo[i] > consumo[menorConsumo]):
        menorConsumo = i
print(f"O menor consumo eh do {veiculos[menorConsumo]}")