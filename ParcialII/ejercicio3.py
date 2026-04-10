# 1. Variable con el texto exacto
cadena3 = "ING. Jefersson Javier Galdámez Mejía"

# 2. Elimina el prefijo sin dejar espacios residuales
sin_ing = cadena3.removeprefix("ING. ")

# 3. Resultado en mayúsculas
print(sin_ing.upper())