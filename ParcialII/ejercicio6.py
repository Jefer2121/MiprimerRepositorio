# 1. Texto base
texto6 = "Jefersson"

# 2. Normalización fuerte
normalizado = texto6.casefold()

# 3. Validación alfabética
resultado6 = normalizado.isalpha()

print(f"¿Es alfabético?: {resultado6}")