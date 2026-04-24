numeros = []
suma = 0

while suma <= 100:
    num = int(input("Ingresa un numero: "))
    
    if num < 0:
        print("Numero negativo, ignorado.")
        continue
    
    numeros.append(num)
    suma += num
    print(f"Suma actual: {suma}")

print(f"\nSuma total supero 100: {suma}")
print("Numeros validos ingresados:")
for n in numeros:
    print(n)