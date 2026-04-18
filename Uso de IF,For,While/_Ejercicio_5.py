n1 = int(input("Primer numero: "))
n2 = int(input("Segundo numero: "))
op = input("Operacion (+, -, *, /): ")

if op == "+":
    print("Resultado:", n1 + n2)
elif op == "-":
    print("Resultado:", n1 - n2)
elif op == "*":
    print("Resultado:", n1 * n2)
elif op == "/":
    if n2 != 0:
        print("Resultado entero:", n1 // n2)
    else:
        print("Error: No se puede dividir entre cero")