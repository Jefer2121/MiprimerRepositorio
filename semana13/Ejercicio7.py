notas = []

while True:
    nota = float(input("Ingresa una nota (-1 para salir): "))
    
    if nota == -1:
        break
    
    if nota < 0 or nota > 10:
        print("Nota invalida, ignorada.")
    else:
        notas.append(nota)

if len(notas) > 0:
    suma = 0
    for n in notas:
        suma += n
    promedio = suma / len(notas)
    print(f"\nPromedio: {promedio:.2f}")
else:
    print("No ingresaste notas validas.")