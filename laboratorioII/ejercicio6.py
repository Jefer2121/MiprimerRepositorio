## Crear una funcion que rexiba un texto y un numero
# transforme el texto segun la opcion y luego devuelva la cantidad de caracteres del resultado
def analizar_grito(grito):
    print(" CONTEO DE LETRAS ")
    resultado = grito.upper()
    print(f"Grito: {resultado}")
    print(f"Longitud del grito: {len(resultado)} caracteres")

analizar_grito("Goooool de la Selecta")