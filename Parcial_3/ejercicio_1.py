# Ejercicio 1: Slicing y Ternario
etiqueta = input("Ingresa el código de rastreo (AÑO-CATEGORIA-PAIS): ")

if etiqueta == "" or etiqueta is None:
    print("Error: entrada vacía o inválida. Finalizando.")
else:
    categoria = etiqueta[5:-3]  # Slicing exacto para extraer categoría
    print(f"Categoría: {categoria}")
    
    pais = etiqueta[-2:]  # Slicing para el país
    ruta = "Ruta Local" if pais == "SV" else "Ruta Internacional"  # Ternario en una línea
    print(ruta)