## Crear una funcion que reciba un texto y un numero 
# si el numero no es 1, 2 o 3 debe mostrar un mensaje de "opcion invalida"
def validar_estadio(nombre, opcion):
    print(" VALIDACION ")
    if opcion not in [1, 2, 3]:
        print(f"Error: La opción {opcion} no existe para el estadio {nombre}")
    else:
        if opcion == 1: print(f"Estadio: {nombre.upper()}")
        elif opcion == 2: print(f"Estadio: {nombre.lower()}")
        else: print(f"Estadio: {nombre.capitalize()}")

# Prueba con el Cuscatlán y una opción inválida (5)
validar_estadio("Cuscatlan", 5)
validar_estadio("Santiago Bernabeu", 1)