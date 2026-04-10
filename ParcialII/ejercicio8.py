# 1. Bloque de texto de 3 líneas
poema = """En el campo verde
corre el balón
metiendo un gol"""

# 2. Contar letra "a"
conteo_a = poema.count("a")

# 3. Dividir por saltos de línea para crear una lista
lista_oraciones = poema.splitlines()

print(f"Letras 'a': {conteo_a}")
print(f"Lista de oraciones: {lista_oraciones}")