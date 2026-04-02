## Solicitar al usuario un texto y un numero
## enviar esos datos a una funcion que aplique la transformacion segun la opcion elegida 
def transformar_frase_corta():
    # Frase configurada
    frase = "El futbol es hermoso"
    
    # Opción elegida: 1 (Para que salga todo en MAYÚSCULAS)
    opcion = 1
    
    print(" MODO FUTBOL ")
    print(f"Frase original: {frase}")

    if opcion == 1:
        resultado = frase.upper()
        print(f"Resultado final: {resultado}")
    elif opcion == 2:
        resultado = frase.lower()
        print(f"Resultado final: {resultado}")
    elif opcion == 3:
        resultado = frase.capitalize()
        print(f"Resultado final: {resultado}")
    else:
        print("Error: Opción no válida")

# Ejecutamos la función directamente
transformar_frase_corta()