# 1. Toma el nombre de archivo 
archivo12 = "ING. Jefersson Javier Galdámez Mejía.txt"

# 2. Remueve sufijo ".txt" y prefijo "ING. "
sin_sufijo = archivo12.removesuffix(".txt")
limpio = sin_sufijo.removeprefix("ING. ")

# 3. Convertir lo que quede a minúsculas
resultado12 = limpio.lower()

print(f"Resultado final: {resultado12}")