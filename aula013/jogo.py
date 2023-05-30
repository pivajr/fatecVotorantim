from funcoes import rola_dado
from time import sleep

while True:
    entrada = input("Digite <Enter> para rolar o seu dado...")
    usuario = rola_dado()
    print("Agora é minha vez de jogar ...")
    for i in range(3):
        for s in range(3):
            print(".", end='')
            sleep(0.5)
        print("        ", end='\r')
    print(" ")
    computador = rola_dado()
    print(f"Você: {usuario} -  Eu: {computador}")
    if usuario > computador:
        print("Você ganhou!!!")
    elif computador == usuario:
        print("Empatamos!!")
    else:
        print("Eu ganhei!!!")
    opcao = input("Você gostaria de jogar novamente <S/N>: ")
    if opcao.upper() == "N":
        break
print("Obrigado por Jogar!!  Agora vá estudar!!!")