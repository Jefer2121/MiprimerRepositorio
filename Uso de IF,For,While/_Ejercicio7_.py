monto = int(input("Monto de la compra: "))
if monto > 100:
    total = int(monto * 0.80)
    print("Descuento del 20%. Total:", total)
elif monto >= 50:
    total = int(monto * 0.90)
    print("Descuento del 10%. Total:", total)
else:
    print("Sin descuento. Total:", monto)