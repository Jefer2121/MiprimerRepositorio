# 1. Declarar variable
cadena = " elefante "

# 2. Eliminar espacios en blanco a los extremos
cadena_limpia = cadena.strip()

# 3. Contar cuántas veces se repite la letra "e"
conteo_e = cadena_limpia.count("e")

print(f"Texto limpio: '{cadena_limpia}'")
print(f"La letra 'e' se repite: {conteo_e} veces")