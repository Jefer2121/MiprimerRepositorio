def suma_pares(numeros):
    total = 0
    for n in numeros:
        if n % 2 == 0:
            total += n
    return total

lista = [1, 2, 3, 4, 5, 6, 8, 11]
print("Suma de pares:", suma_pares(lista))