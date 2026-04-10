# 1. Toma la cadena con espacios
cadena11 = " el nido matinal "

# 2. Limpia extremos y pon iniciales en mayúscula
limpio = cadena11.strip()
formato_titulo = limpio.title()

# 3. Centrar en 30 caracteres con guiones "-"
resultado11 = formato_titulo.center(30, "-")

# Imprime el resultado (Asegúrate de poner la comilla al final)
print(f"{resultado11}")
