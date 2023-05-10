t = ()
for i in range(5):
    x = int(input("Digite um valor: "))
    t = t + tuple([x])
# mostra a tupla na ordem inversa
print(t[::-1])
