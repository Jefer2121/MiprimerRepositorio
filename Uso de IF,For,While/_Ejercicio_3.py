nota = int(input("Ingrese una nota (0-10): "))
if nota >= 9 and nota <= 10:
    print("Excelente")
elif nota >= 7 and nota <= 8:
    print("Bueno")
elif nota == 6:
    print("Aprobado")
else:
    print("Reprobado")