print("===== CALCULADORA =====")
print("=======================")
v1 = float(input("Valor1: "))
v2 = float(input("Valor2: "))
op = input("Operação? (+,-,/,*): ")
if op == '+':
    print("Resultado: ", v1 + v2)
elif op == '-':
    print("Resultado: ", v1 - v2)
elif op == '/':
    print("Resultado: ", v1 / v2)
elif op == '*':
    print("Resultado: ", v1 * v2)
else:
    print("Operação Inválida!!")
print("=======================")