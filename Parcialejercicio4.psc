Algoritmo NumerosNpares
    // Definimos las variables necesarias para el conteo
    Definir cantidad, contador Como Entero
    
    Escribir " Bienvenido al generador de pares "
    Escribir "Dime cuántos números pares deseas ver hoy:"
    Leer cantidad
    
    Si cantidad <= 0 Entonces
        Escribir " ingresa un número mayor a cero para poder trabajar."
    Sino
        Escribir "Aquí tienes los primeros ", cantidad, " números pares:"
        // El bucle Para se encarga de repetir la multiplicación por 2
        Para contador <- 1 Hasta cantidad Con Paso 1 Hacer
            Escribir "Par número ", contador, ": ", contador * 2
        FinPara
        Escribir "Proceso finalizado con éxito."
    FinSi
FinAlgoritmo