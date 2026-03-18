# las comillas triples son las que se encargan de hacer 
# Cadenas de texto largas sin mdoficar el formato.
#texto corto
cancion= "  "

#textos largos ''' o """    
cancion= """Tu mi locura, baby (baby)
Pasan las horas y mas me pide mas (mas)
No se cansa, parece no tener final
lo nuestro es una locura 

Siempre que escucho una cancion que me recuerda a ti
O una foto tuya atrevida que me llega a mi
Me activa el deseo, de ti me dan gana
Y te llamo porque se que lo quitaba """

#print(cancion)

## computadora -> que variable queres limpiar
## print() =>
# void -> no devuelve un tipo de dato  
# objeto -> devuelve un tipo de dato

## realizar una wiki tambien puede darle doble clic documento y se les
## despligar el editor de texto

# poema es un espacio de memoria para string
# se va a llenar con el contenido de poema alterar con la accion upper (mayusculas)
cancion_Mayusculas = cancion.upper()
#print(cancion_Mayusculas)

# convertir en minusculas
## string lower 

cancion_minusculas = cancion. lower()
print(cancion_minusculas)

## tiene que ingresar 100 nombres en mayusculas
mensaje = "hola kace progamando o que hace" 
## Capitalize  a que la primera letra de cada palabra sea mayusculas
mensajeCorrecto = mensaje.capitalize()
#print(mensajeCorrecto)

## las flipantes aventuras del gato con bolson magico y alfredo
titulo = "las flipantes aventuras del gato con bolson magico y alfredo" 
tituloCorrecto = titulo.title()
#print(tituloCorrecto)

## swapcase() permite cambiar entre mayusculas y minusculas 
swapCaseTitulo = tituloCorrecto.swapcase()
print(swapCaseTitulo)

# metodos de validacion 
# false numeros o espacio
# true tiene solo letras

numero = "512"
solo_letras = "El chico del apartamento"
coro = "piribiri_ban_ban" 

quieroSololetras = solo_letras.isalpha()
print(quieroSololetras)

## numeros y letras 
print("numeros y letras")
numeros_letras = nombre + numero
evaluarTexto = numeros_letras.isalnum()
print(evaluarTexto)