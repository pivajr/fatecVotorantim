arquivo = open("frutas.txt", "w", encoding="utf-8")
while True:
    fruta = input("Digite uma fruta: ")
    if fruta == '':
        break
    arquivo.write(f"{fruta}\n")
arquivo.close()
