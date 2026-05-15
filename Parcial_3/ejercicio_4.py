# Ejercicio 4: Auditoria
for numero in range(1, 51):
    if numero == 42:
        print("¡Amenaza detectada! Deteniendo auditoría.")
        break
    if numero % 3 == 0:
        continue
    print(f"Procesando registro ID: {numero}")