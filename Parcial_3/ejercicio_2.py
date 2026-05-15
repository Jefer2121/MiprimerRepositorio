# Ejercicio 2: Cobro Seguro
from decimal import Decimal

total = Decimal("0")

while True:
    entrada = input("Ingresa precio del producto (0 para salir): ")
    try:
        precio = Decimal(entrada)
        if precio == 0:
            break
        total += precio
        print(f"Precio registrado: {precio}")
    except ValueError:
        print("Advertencia: ingresa un número válido.")

print(f"Total acumulado: {total}")