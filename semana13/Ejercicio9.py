import random

numero_secreto = random.randint(1, 100)
intentos = []

while True:
    intento = int(input("Adivina el numero (1-100): "))
    intentos.append(intento)
    
    if intento == numero_secreto:
        print("Correcto!")
        break
    elif intento < numero_secreto:
        print("El numero es mayor.")
    else:
        print("El numero es menor.")

print(f"\nIntentos realizados: {len(intentos)}")
for i in range(len(intentos)):
    print(f"Intento {i+1}: {intentos[i]}")