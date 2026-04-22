

## Van a crear una funcion que valide si el nombres esta en mayuscula
# mayuscula true
# minuscula false

entradaDeDatos = input("Messi la cabra: ")


def validarMayusculas(entradaDeDatos):
    validar = entradaDeDatos.isupper()
    return validar


print(validarMayusculas(entradaDeDatos))