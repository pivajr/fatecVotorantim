largura = float(input("Largura do aposento: "))
comprimento = float(input("Comprimento do aposento: "))
altura = 2.8
volume_lata = input("Volume lata: (A)-1 litro (B)-3.6 litros e (C)-18 litros: ")
area_porta = 0.8 * 2.1
rendimento = 3
if volume_lata.upper() == 'A':
    volume_lata = 1
else:
    if volume_lata.upper() == 'B':
        volume_lata = 3.6
    else:
        if volume_lata.upper() == 'C':
            volume_lata = 18
        else:
            volume_lata = 1

area = (largura * altura * 2) + (comprimento * altura * 2)
area = area - area_porta

litros_necessarios = area / rendimento

qtd_latas = litros_necessarios / volume_lata

if (qtd_latas - int(qtd_latas)) > 0:
    qtd_latas = int(qtd_latas) + 1

print(f"Qtd latas necessárias: {qtd_latas}")
