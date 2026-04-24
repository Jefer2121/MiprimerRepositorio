# Ejercicio 2: Contador de positivos y negativos
positivos = 0
negativos = 0

while True:
    num = int(input("Ingrese un número (0 para salir): "))
    
    if num == 0:
        break
    
    if num > 0:
        positivos += 1
    else:
        negativos += 1

print("\n--- RESUMEN DE RESULTADOS ---")
resumen = [f"Cantidad de positivos: {positivos}", f"Cantidad de negativos: {negativos}"]

for resultado in resumen:
    print(resultado)