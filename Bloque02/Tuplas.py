#Tuplas

#Listas inmutables, es decir, que no pueden ser modificadas después de su creación
#Extraer porciones de la misma
#Permite realizar búsquedas
#Puedo ver si un elemento x se encuentra dentro de la tupla

#Son más rápidas en su ejecución
#Necesitan menos espacio
#Aconsejables de usar cuando hablamos de recorridos
#Formatear cadenas de caracteres
#Se pueden utilizar como claves para diccionarios

#Declaracion

metodos = ("Index", "len")

# Empaquetado de tuplas
lenguajes = "Ruby", "Python", "JavaScript"
#               0       1           2
a = 2

b = 3

c = 5

letras = 2, 3, 5

#Consultando la tupla
print(metodos[0])

#Creando una lista nueva a partir de una tupla
lista_lenguajes = list(lenguajes)
print(f"Tupla: {lenguajes}\tLista: {lista_lenguajes}")
lista_lenguajes.append("Elixir")

#Creando una tupla a partir de una lista

lenguajes = tuple(lista_lenguajes)
print(f"Nueva Tupla: {lenguajes}")

#Tupla de tuplas
tupla2 = (1,2)
tupla = (tupla2,("Uno", "Dos"))


print(f"{tupla[tupla.index(tupla2)].index(2)}")

#Asignar valores de la tupla a variables

rb, py, js, ex = lenguajes

print(f"Rb {rb} py {py} js {js} ex{ex}")


#tupla unitaria
tupla_unitaria = ("Mamberroi",)




