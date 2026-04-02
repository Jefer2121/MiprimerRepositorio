## Crear una funcion que reciba una lista de palabras y un numero 
## la funcion debe transformar cada palabra de la lista segun la opcion seleccionada (1,2 o 3)
def transformar_equipos(lista, numero):
    print(" LISTA DE EQUIPOS ")
    nueva_lista = []
    for equipo in lista:
        if numero == 1:
            nueva_lista.append(equipo.upper())
        else:
            nueva_lista.append(equipo.lower())
    print(f"Resultado: {nueva_lista}")

# Datos fijos: Equipos de El Salvador y España
mis_equipos = ["Alianza", "FAS", "Real Madrid", "Barcelona"]
transformar_equipos(mis_equipos, 1)