##  Crear una funcion que reciba una palabra y un numero y muestre el resultado en pantalla 
## aplicando la transformacion correspondiente (1,2 o 3)
def mostrar_resultado(palabra, numero):
    if numero == 1:
        res = palabra.upper()
    elif numero == 2:
        res = palabra.lower()
    else:
        res = palabra.capitalize()
    print(f"El resultado es: {res}")

# Prueba
mostrar_resultado("Sistemas", 1)