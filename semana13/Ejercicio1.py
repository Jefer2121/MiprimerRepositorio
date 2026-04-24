while True:
    n = int(input("Ingrese un número n (0 para salir): "))
    if n == 0:
        break
    
    print(f"Números pares del 1 al {n}:")
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)