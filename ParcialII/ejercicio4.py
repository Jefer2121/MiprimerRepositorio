# 1. Palabra base
palabra4 = "CANTANDO"

# 2. Conversión a minúsculas
minusc = palabra4.lower()

# 3. Elimina sufijo y encuentra el índice de la "t"
sin_sufijo = minusc.removesuffix("ando")
indice_t = minusc.find("t")

print(f"Texto: {sin_sufijo}, Indice: {indice_t}")