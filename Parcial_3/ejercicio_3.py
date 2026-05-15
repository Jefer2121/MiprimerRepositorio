# Ejercicio 3: Sensor IoT
temperaturas = []

for i in range(5):
    temp = int(input(f"Lectura {i+1}: "))
    temperaturas.append(temp)

for temp in temperaturas:
    match temp:
        case 0:
            print("Alerta: Punto de Congelación")
        case 100:
            print("Alerta: Punto de Ebullición")
        case _:
            estado = "Estado: Estable" if 10 <= temp <= 30 else "Estado: Crítico"
            print(estado)