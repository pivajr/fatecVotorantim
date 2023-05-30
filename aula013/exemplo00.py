def fatorial(n):
    if n > 1:
        return n * fatorial(n-1)
    else:
        return 1

x = int(input("Digite um número: "))
print(f"{x}! = {fatorial(x)}")