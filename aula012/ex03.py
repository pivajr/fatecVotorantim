def bissexto(n):
    if (n % 4) == 0:
        if (n % 100) == 0:
            if (n % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

n = int(input("Digite ano: "))
if bissexto(n):
    print("Ano Bissexto!")
else:
    print("Ano não Bissexto!")


