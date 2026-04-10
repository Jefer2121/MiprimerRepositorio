Algoritmo Sumarhastapar
	// Sumar hasta que el total sea par usando variable logico
	//  PUNTO 1: DECLARACIÓN DE VARIABLES (Entero, Real y Lógico) 
	Definir total, numeroIngresado Como Entero;
	Definir promedioFicticio Como Real; 
	Definir esPar, continuar Como Logico;
	
	// PUNTO 2: NOMBRES COHERENTES E INICIALIZACIÓN 
	total <- 0;
	promedioFicticio <- 0.0;
	esPar <- Falso; // PUNTO 5: Valor Booleano inicial
	continuar <- Verdadero;
	
	Escribir " Bienvenido al Acumulador Par ";
	
	//  PUNTO 3: ESTRUCTURA REPETITIVA HACER-MIENTRAS (Repetir) 
	Repetir
		
		//  PUNTO 6: ENTRADA DE DATOS MEDIANTE LEER 
		Escribir "Ingrese un numero para sumar:";
		Leer numeroIngresado;
		
		// PUNTO 7: OPERACIONES MATEMÁTICAS BÁSICAS (Sumar) 
		total <- total + numeroIngresado;
		Escribir "Suma actual: ", total;
		
		// PUNTO 4: USO DE OPERADORES LÓGICOS (Y, O, NO) 
		
		// Uso del operador Y:
		Si (total MOD 2 = 0) Y (total > 0) Entonces
			esPar <- Verdadero; // PUNTO 5: Valor Booleano
		FinSi
		
		// Uso del operador NO y O:
		// Si NO es par O el total es cero, debemos seguir
		Si NO (esPar) O (total = 0) Entonces
			Escribir "El total sigue siendo impar o cero. Continue...";
			continuar <- Verdadero;
		Sino
			Escribir "¡Meta alcanzada! El total es par.";
			continuar <- Falso;
		FinSi
		
	Hasta Que continuar = Falso; // PUNTO 8: Lógica algorítmica funcional
	
	// Resultado final
	Escribir "El proceso ha terminado. El total final es: ", total;
	
FinAlgoritmo
	
