def solo_positivos(numeros):
    positivos = []
    for n in numeros:
        if n > 0:
            positivos.append(n)
    return positivos

lista = [3, -1, 7, -5, 0, 2, -8, 9]
print("Positivos:", solo_positivos(lista))