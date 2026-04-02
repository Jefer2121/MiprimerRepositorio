## Crear una funcion que reciba un texto y una lista de numeros (entre 1 y 3)
# la funcion debe aplicar cada transformacion en orden y devolver el resultado final
def procesar_jugador(nombre):
    print("  PROCESAMIENTO ")
    paso1 = nombre.upper()      # Todo a mayúsculas
    paso2 = paso1.capitalize() # Solo la primera letra
    print(f"Original: {nombre}")
    print(f"Paso 1 (MAYUS): {paso1}")
    print(f"Paso 2 (Capital): {paso2}")

procesar_jugador("lionel messi")