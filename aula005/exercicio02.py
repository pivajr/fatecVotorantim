p1 = float(input("Nota Prova1: "))
p2 = float(input("Nota Prova2: "))
p3 = float(input("Nota Prova3: "))
media = (p1 + p2 + p3) / 3
if media >= 7:
    print("Aprovado!")
else:
    if media < 3:
        print("Reprovado!")
    else:
        print("Exame!")
        nota = 12 - media
        print(f"Você tem que tirar no mínimo {nota:.1f}")