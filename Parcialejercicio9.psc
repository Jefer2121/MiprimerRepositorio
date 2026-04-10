Algoritmo Ejercicio9_DivisibilidadOr

    // Emplea el operador 'OR' para validar si un valor es múltiplo de 3 o 5.
    // Utiliza 'MOD' para determinar el residuo con precisión matemática.
    Definir n Como Entero
    Escribir "Ingrese número entero para verificar divisibilidad:"
    Leer n
    
    Si n % 3 = 0 O n % 5 = 0 Entonces
        Escribir "Resultado: El número es divisible por 3 o por 5."
    Sino
        Escribir "Resultado: El número no cumple con los criterios de divisibilidad."
    FinSi
FinAlgoritmo