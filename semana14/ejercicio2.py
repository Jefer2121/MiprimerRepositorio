def filtrar_nombres(nombres):
    for nombre in nombres:
        if len(nombre) > 5:
            print(nombre)

nombres = ["Ana", "Camila", "Luis", "Valentina", "Pedro", "Sebastián", "Eva", "Natalia", "Sol", "Andrés"]
filtrar_nombres(nombres)