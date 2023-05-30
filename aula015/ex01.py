# Abre o arquivo para leitura
arquivoEntrada = open('empregados.txt')
# Coloca todas as linhas em memoria
linhas = arquivoEntrada.readlines()
# Fecha o arquivo
arquivoEntrada.close()
linhas.sort()
print(linhas)

usuarios = []
espacos_utilizados = []
espaco_total = 0.0
for linha in linhas:
    campos = linha.split()
    usuario = campos[0]
    espaco_utilizado = int(campos[1])
    usuarios.append(usuario)
    espacos_utilizados.append(espaco_utilizado)
    espaco_total += espaco_utilizado

# Definição dos Textos e valores
l1 = 'ACME Inc.               Uso do espaco em disco pelos usuarios\n'
l2 = '-----------------------------------------------------------------------\n'
l3 = 'Nr.  Usuario        Espaco utilizado     %% do uso'
mega = (1024.0 * 1024.0)
# Abre o arquivo para escrita
saida = open('saida_ex1.txt', 'w')
saida.write(l1)
saida.write(l2)
saida.write(l3)
for i in range(len(usuarios)):
    espacoMB = espacos_utilizados[i] / mega
    percentual_uso = espacos_utilizados[i] / espaco_total
    saida.write(f'\n{i+1} - {usuarios[i]:20} - {espacoMB:.2f} - {percentual_uso:.2%}')

saida.write(f'\nEspaco total ocupado: {espaco_total / mega} MB')
saida.write(f'\nEspaco medio ocupado: {(espaco_total / len(usuarios))/ mega} MB')
# Fecha o arquivo
saida.close()
