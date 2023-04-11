nome = input("Entre com o primeiro nome: ")
nome_do_meio = input("Entre com o nome do meio: ")
sobrenome = input("Entre com seu sobrenome: ")
nome_completo = nome + ' ' + nome_do_meio + ' ' + sobrenome

print(f"Nome completo: {nome_completo} !")

# Criptografia
nome_cripto = ''
for indice in range(0, len(nome_completo)):
    nome_cripto += chr( ord(nome_completo[indice])+1 )

print(f"Nome Cripto: {nome_cripto}")