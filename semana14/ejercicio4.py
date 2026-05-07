def numero_mayor(numeros):
    mayor = numeros[0]
    for n in numeros:
        if n > mayor:
            mayor = n
    return mayor

arreglo = [4, 12, 7, 33, 2, 19, 8, 25]
print("El número mayor es:", numero_mayor(arreglo))