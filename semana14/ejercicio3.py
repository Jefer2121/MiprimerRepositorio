def promedio_notas(notas):
    promedio = sum(notas) / len(notas)
    if promedio >= 6:
        estado = "El grupo aprueba"
    else:
        estado = "El grupo reprueba"
    return promedio, estado

notas = [7, 5, 6, 4, 8]
p, e = promedio_notas(notas)
print("Promedio:", p)
print(e)