a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))
if ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    if (a == b) and (b == c):
        print("Triângulo Equilátero")
    else:
        if (a == b) or (b == c) or (a == c):
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
else:
    print("Os valores digitados não formam um triângulo!")

