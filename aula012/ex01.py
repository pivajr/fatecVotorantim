def epar(x):
    return (x % 2 == 0)

n = int(input("Digite um número: "))
if epar(n):
    print("O número é par!")
else:
    print("O número é impar!")

