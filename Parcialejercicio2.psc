Algoritmo SumaPositivos
    Definir num, suma Como Real
    suma <- 0
    
    Escribir "Ingrese un número (negativo para salir):"
    Leer num
    
    Mientras num >= 0 Hacer
        suma <- suma + num
        Escribir "Ingrese otro número (negativo para salir):"
        Leer num
    FinMientras
    
    Escribir "La suma de los números positivos es: ", suma
FinAlgoritmo