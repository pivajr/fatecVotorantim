def pega_sobrenome():
    while True:
        sobrenome = input("Digite o sobrenome: ")
        if sobrenome:
            if sobrenome.isalpha():
                return sobrenome
            else:
                print("Digite um sobrenome válido! ")
        else:
            return sobrenome

def pega_idade():
    while True:
        try:
            idade = int(input("Digite a idade: "))
        except:
            print("Digite uma idade válida! ")
        else:
            if idade:
                return idade
            else:
                print("Digite uma idade válida! ")

def pega_altura():
    while True:
        try:
            altura = int(input("Digite a altura (em centímetros): "))
        except:
            print("Digite uma altura em centímetros válida! ")
        else:
            if altura:
                return altura
            else:
                print("Digite uma altura em centímetros válida! ")

def pega_peso():
    while True:
        try:
            peso = float(input("Digite o peso (em Kg): "))
        except:
            print("Digite um peso em Kg válido! ")
        else:
            if peso:
                return peso
            else:
                print("Digite um peso em Kg válido! ")

pessoas = []
n=0
while True:
    sobrenome = pega_sobrenome()
    if sobrenome:
        n += 1
        idade = pega_idade()
        altura = pega_altura()
        peso = pega_peso()
        pessoa = [sobrenome, idade, altura, peso]
        pessoas.append(pessoa)
    else:
        break

soma_idade = 0
soma_altura = 0
soma_peso = 0
if n>0:
    #Existe 1 ou mais pessoas cadastradas
    pessoas.sort()
    print("Relação de nomes Cadastrados...")
    print("-------------------------------------------------")
    for i in range(0, len(pessoas)):
        print(f"{pessoas[i][0]:10} - {pessoas[i][1]} - {pessoas[i][2]} - {pessoas[i][3]:5.1f}")
        soma_idade += pessoas[i][1]
        soma_altura += pessoas[i][2]
        soma_peso += pessoas[i][3]
    print("-------------------------------------------------")
    media_idade = soma_idade/n
    media_altura = soma_altura/n
    media_peso = soma_peso/n
    print(f"Idade média: {media_idade}")
    print(f"Altura média: {media_altura}")
    print(f"Peso médio: {media_peso}")
    print("-------------------------------------------------")