while True:
    n = int(input("Ingresa un numero n (0 para salir): "))
    
    if n == 0:
        break
    
    print(f"\nNumeros primos del 1 al {n}:")
    for num in range(2, n + 1):
        es_primo = True
        for divisor in range(2, num):
            if num % divisor == 0:
                es_primo = False
                break
        if es_primo:
            print(num)