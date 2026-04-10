Algoritmo operacionesbasicas 
	// Pedir dos numeros 
	// mostrar la suma, la resta, la multiplicacion y division.
    Definir n1, n2, suma, resta, multi, divi Como Real;
    
    // Entrada de datos
    Escribir "Introduce el primer número:";
    Leer n1;
    
    Escribir "Introduce el segundo número:";
    Leer n2;
    
    // Procesos matemáticos
    suma  <- n1 + n2;
    resta <- n1 - n2;
    multi <- n1 * n2;
    
    // Salida de resultados
    Escribir "--- Resultados ---";
    Escribir "La suma es: ", suma;
    Escribir "La resta es: ", resta;
    Escribir "La multiplicación es: ", multi;
    
    // Validación simple para evitar error de división por cero
    Si n2 <> 0 Entonces
        divi <- n1 / n2;
        Escribir "La división es: ", divi;
    Sino
        Escribir "La división no es posible (no se puede dividir por cero).";
    FinSi
FinAlgoritmo
