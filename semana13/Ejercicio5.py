contrasena_correcta = "python123"
intentos_fallidos = []

while True:
    intento = input("Ingresa la contrasena: ")
    
    if intento == contrasena_correcta:
        print("Contrasena correcta!")
        break
    else:
        intentos_fallidos.append(intento)
        print("Contrasena incorrecta, intenta de nuevo.")

print(f"\nIntentos fallidos: {len(intentos_fallidos)}")
for i in range(len(intentos_fallidos)):
    print(f"Intento {i+1}: fallido")