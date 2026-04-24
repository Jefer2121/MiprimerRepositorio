total = 0
while True:
    numero = int(input("Ingrese un número para sumar (0 para finalizar): "))
    if numero == 0:
        break
    total += numero

print(f"La suma total es: {total}")