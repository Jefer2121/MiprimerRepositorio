# 1. Toma la cadena
cadena10 = "Python2026"

# 2. Verifica si es estrictamente alfanumérico
es_alfanumerico = cadena10.isalnum()

# 3. Convertir a minúsculas y separar eliminando "2026"
# La guía pide reemplazar "2026" por una cadena vacía ""
texto_min = cadena10.lower()
solo_palabra = texto_min.replace("2026", "")

print(f"¿Es alfanumérico?: {es_alfanumerico}")
print(f"Palabra resultante: {solo_palabra}")