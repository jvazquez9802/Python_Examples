#UN TIPO DE DATO COMPUESTO CONTIENE UNA COLECCION DE ELEMENTOS

#CADENAS DE CARACTERES -> Secuencia inmutable de caracteres delimitada por comillas
#dobles o sencillas.

cadena = 'Cadena de ejemplo'
cadena2 = "Cadena de ejemplo"
cadena3 = """ Cadena larga """

#Setencias de escape
# \n Salto de linea
# \\ Mostrar un diagonal invertido
# \t Una tabulación
# \' Mostrar la comilla como delimitante
# \" Mostrar la comilla como delimitante
#\b Elimina el caracter anterior

#Cadena de caracteres cruda, se muestra tal cual es definida
miNombre = r"\tHola\n Juan \\"

#len() Nos ayuda a conocer cuantos elementos existen en nuestra coleccion
#print(len(cadena))

#LISTAS
#Pueden guardar datos de diferentes tipos
#Las listas son dinamicas, es decir puedo agregar y quitar elementos segun se requiera
#Son mutables

#asignar un nombre = []

lista = []
numeros = [1, 2, [3.0,4.0], "uno", "dos"]
#Indice    0  1      2         3     4
#Indice  -5  -4     -3        -2    -1

#Lista de listas -> Matriz
letras = [['a','b','c'],['d','e','f']]

#print(letras[-1][-2])
"""
   0 1 2
0 |a b c|
1 |d e f|
"""

#Muchas listas wuuuuu
lista = [['a',['4',['c',['3'],[2,3,4,5,2]]]]]

#print(int(lista[0][1][1][1][0]) + lista[0][1][1][2][0])
#Salida 5
#<int> ArrayList nombre = new <int>;

#Metodos con listas
print("Resultados metodos con listas")
animales = ["Gato", "Perro", "Hámster", "Iguana", "Gato"]
print(f"Len {len(animales)}") #Cantidad de elementos que existen en mi lista
animales.append("Huachinango") #append agrega elementos a la lista
print(f"Count {animales.count('Gato')}") #Contar las veces que aparece un elemento
#extend agregar un iterador a un rango
#animales.extend(2,9)
#Index regresa el indice en donde se encuentra un elemento por primera vez
print(f"index {animales.index('Gato')}")
animal = "Hipopotamo"
animales.insert(2,animal)
animales.insert(2,animal)
print(f"lista despues de insertar a {animal} = {animales}")
#Eliminar al ultimo elemento
print(f"Antes de eliminar = {animales}")
#Si nosotros queremos eliminar un elemento por su indice
#el metodo pop recibe el indice como argumento
print(f"{animales.pop()} Despues de eliminar = {animales}")
#Eliminar un elemento deseado
print(f"METODO REMOVE\nAntes {animales}")
print(f"{animales.remove(animal)} <=> Despues {animales}")

#Invierte el orden de los elementos
animales.reverse()
print(animales)

listaNumerica = [10, 7, 4, 5, 8, 1]
print(listaNumerica)
listaNumerica.sort()
print(f"Despues de ordenar {listaNumerica}")

listaNumerica.sort(reverse=True)
print(f"Despues de ordenar invertido {listaNumerica}")

#Para modificar un valor en una lista necesitamos especificar 
#Nombre[indice] = nuevo valor

#Ejemplo de lista en Java
# int [] nombre = new int[tamaño];
# int [][] numeros = new int[10][10];

#TUPLAS

#DICCIONARIOS