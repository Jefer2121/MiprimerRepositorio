Algoritmo ValidarRangoInteractiva
    // algoritmo que solicite un numero entre 1 y 10
    // y continue pidiendo hasta que el usuario ingrese un numero invalido
	// usando la estructura mientas (hacer mientras o hacer)
    Definir n Como Real
    Escribir "--- Validador de Seguridad de Rango ---"
    Escribir "El sistema solo aceptará valores enteros o decimales entre 1 y 10."
    Leer n
    // El bucle se mantiene vivo siempre que el usuario respete el contrato de datos.
    Mientras n >= 1 Y n <= 10 Hacer
        Escribir "Estado: Valor ", n, " validado correctamente."
        Escribir "Ingrese el siguiente valor para continuar (o uno fuera de rango para cerrar):"
        Leer n
    FinMientras
    // Si el usuario ingresa algo como 11 o 0, el bucle se rompe.
    Escribir "ALERTA: El valor ingresado (", n, ") está fuera del rango permitido."
    Escribir "Cerrando sistema de validación de forma segura..."
FinAlgoritmo