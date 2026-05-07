def mayores_de_edad(edades):
    contador = 0
    for edad in edades:
        if edad >= 18:
            contador += 1
    return contador

edades = [15, 20, 17, 22, 14, 30, 18, 16]
print("Mayores de edad:", mayores_de_edad(edades))