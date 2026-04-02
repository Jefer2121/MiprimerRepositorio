## Crear una funcion que reciba un texto y un numero. segun el numero
# convetir todo el texto a mayusculas
# convertir todo el texto a minusculas
# colocar la primera letra en mayusculas
def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return texto

# Ejemplo de uso
print(transformar_texto("hola mundo", 1))