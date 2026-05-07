def ordenar(numeros):
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] > numeros[j]:
                numeros[i], numeros[j] = numeros[j], numeros[i]
    return numeros

arreglo = [5, 2, 8, 1, 9, 3]
print("Ordenados:", ordenar(arreglo))