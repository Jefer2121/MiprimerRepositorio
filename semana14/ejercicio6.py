import random

def mayores_a_50(numeros):
    contador = 0
    for n in numeros:
        if n > 50:
            contador += 1
    return contador

random.seed(42)
arreglo = [random.randint(1, 100) for _ in range(10)]
print("Números:", arreglo)
print("Mayores a 50:", mayores_a_50(arreglo))