# Ejercicio 5: Privacidad
nombre_completo = input("Ingresa tu nombre completo (Nombre Apellido): ")

partes = nombre_completo.split()
invertido = partes[::-1]

for palabra in invertido:
    letras = ""
    for letra in palabra:
        letras += letra + "."
    print(letras[:-1])