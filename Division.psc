Algoritmo sin_titulo
	// Solicitar al usuario dos números
	// y mostrar el resultado de la división del primero entre el segundo.
	// Validar que el segundo número no sea cero.
	Definir NumeroEntrada1, NumeroEntrada2, Resultado Como Real;
	Escribir ' Ingrese el primer número (dividendo): ';
	Leer NumeroEntrada1;
	Escribir ' Ingrese el segundo número (divisor): ';
	Leer NumeroEntrada2;
	
	// La condición lógica valida que el divisor no sea 0
	Si NumeroEntrada2 <> 0 Entonces
		Resultado = NumeroEntrada1 / NumeroEntrada2;
		Escribir 'El resultado de la división es: ', Resultado;
	Sino
		Escribir 'Error: No se puede dividir entre cero.';
	FinSi
FinAlgoritmo
