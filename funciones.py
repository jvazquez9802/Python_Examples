#Una funcion es un bloloque de codigo reutilizable se encarga de una determinada tarea

#Modular nuestra aplicacion, segmentar modulos mas simples nuestro codigo
#Reutilzables, permite utilizar unja misma funcion en distintos programas
#Nos brindan soluciones generales

def mi_funcion():
    return "Hola Mundo"

print(mi_funcion())

def mi_funcion2():
    print("Hola mundo desde la función")
    

#Clasificacion de las funciones
#Procedimientos cuando es una funcion que realiza una tarea pero no retorna un valor
#Funcion cuando retorna un valor
#Metodo cuando la funcion esta declarada en el contexto de una clase y necesita ser
#    llamada a traves de un objeto
    
    
#funcion con parametros
"""
def mi_funcion_con_parametros(arg1, arg2):
    return int(arg1) + int(arg2)

print(mi_funcion_con_parametros(input("Dame el primer numero"), input("Dame el segundo numero")))

num1 = input("Dame el primer numero")
num2 = input("Dame el segundo numero")
resultado = mi_funcion_con_parametros(num1, num2)
print(resultado)
"""
#Podemos utilizar la palabra reservada pass para dejar una funcion sin cuerpo
def funcion_vacia():
    pass

#Funcion anidada - nested function
#Una función que está contenida dentro de otra función

def funcion_principal():
    
    def funcion_anidada():
        print("Soy la funcion anidada 1")
        
    def funcion_anidada2():
        print("Soy la funcion anidada 2")
    
    funcion_anidada()
    funcion_anidada2()
funcion_principal()

#funcion como un objeto
def funcion_ejemplo():
    return("Funcion como objeto desde funciones")

print(funcion_ejemplo)

g = funcion_ejemplo

def funcion_ejemplo_2(parametro):
    print(parametro())
    
funcion_ejemplo_2(g)

#print(mi_funcion())
#NameSpace -> Sistema que permite gestionar los nombres de mis variables y funciones
#Rule LGEB
#Ver tipos_datos.py para este ejemplo

import tipos_datos
print(tipos_datos.funcion_ejemplo())
print(funcion_ejemplo)

#Built-in
    #Global
        #Enclose
            #Local

#Uso de global
print("Esta linea esta en global")
variable = 10

def _funcion_principal():
    global variable
    variable += 5
    print("Esta linea esta en local\n" + str(variable))
    
#_funcion_principal()
#print(variable)

#Uso de enclose

var = 5
def funcion_outer():
    var = 10
    def funcion_inner():
        nonlocal var 
        var += 15
        print(var)
    funcion_inner()
    print(var)
funcion_outer()
print(var)

#Closure -> Mantener valores a pesar de que estos dejen de existir

def outer():
    x = 5
    def inner():
        print(x)
        return x
    return inner

g = outer()
print(g())