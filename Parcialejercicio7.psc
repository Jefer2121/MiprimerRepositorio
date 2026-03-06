Algoritmo ProductoYCociente
    //  solicitar dos numeros y mostrar el producto y cociente
	//evitar la division entre 0

    Definir v1, v2 Como Real
    
    Escribir " Calculadora de Producto y Cociente "
    Escribir "Ingrese el primer número:"
    Leer v1
    Escribir "Ingrese el segundo número:"
    Leer v2
    
    // Cálculo directo del producto
    Escribir ">> El producto es: ", v1 * v2
    
    // Cálculo del cociente con validación de seguridad
    Si v2 <> 0 Entonces
        Escribir ">> El cociente es: ", v1 / v2
    Sino
        Escribir ">> Error: No es posible realizar la división entre cero."
    FinSi
    
    Escribir "Operación finalizada."
FinAlgoritmo