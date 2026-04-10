# 1. Texto numérico
texto7 = "42"

# 2. Rellenar con ceros a la izquierda hasta 5 caracteres
relleno = texto7.zfill(5)

# 3. Verificar si termina en "2" (booleano)
termina_en_dos = relleno.endswith("2")

print(f"Resultado: {relleno}, ¿Termina en 2?: {termina_en_dos}")