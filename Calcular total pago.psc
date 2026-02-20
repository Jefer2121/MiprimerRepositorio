Algoritmo calculartotalpago
	// Solicitar el precio de un producto
	// la cantidad comprada, luego calcular y mostrar el total a pagar
	Definir precio, cantidad, total Como Real
	// Entrada de datos
	Escribir 'Ingrese el precio del producto:'
	Leer precio
	Escribir 'Ingrese la cantidad comprada:'
	Leer cantidad
	// Proceso: Multiplicación del precio por la cantidad
	total <- precio*cantidad
	// Salida de resultados
	Escribir '---------------------------------'
	Escribir 'El total a pagar es: $', total
	Escribir '---------------------------------'
FinAlgoritmo
