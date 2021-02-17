#Diccionarios

#Nos permiten guardar o almacenar diversos tipos de datos

#No se utilizan indices, los elementos son almacenados mediante una relación
#de clave:valor para cada uno de los elementos

#Cuando trabajo con diccionarios es indiferente el orden de los elementos porque se trabaja
#con claves únicas

#Para definir un diccionario, se encierra el listado de valores entre llaves, las parejas
#se separan por comas, la clave y el valor se separan por dos puntos

alumnos = []

alumno = {"nombre":"Juan", "edad":22, "telefono":{"movil":3121122913, "hogar":3121122811}}
alumnos.append(alumno)

print(f"Nombre: {alumno['nombre']} telefono movil: {alumno['telefono']['movil']}")

"""nombre = input("Ingresa nombre")
edad = input("Ingresa edad")
movil = input("Ingresa movil")
hogar = input("Ingresa hogar")"""

"""alumno2 = {"nombre":nombre, "edad":edad, "telefono":{"movil":movil, "hogar":hogar}}
alumnos.append(alumno2)"""

print(alumnos)

alumnos_tec =\
{
    "17460654":\
        {
            "nombre-completo":"Juan Luis Vázquez Hernández",
            "carrera":"Informática",
            "semestre":8
        },
    "17460765":\
    {
        "nombre-completo":"Luis Juan Hernández Vázquez ",
        "carrera":"Sistemas",
        "semestre":8
    }
}

print(f"Carrera de 17460654: {alumnos_tec['17460654']['carrera']}")

#Metodos con diccionarios

# dict -> Recibir una representación de un diccionario y crearlo si es factible
dic = dict(nombre="Jose", edad=25, carrera="arquitectura")
print(dic)

#Recibir dos secuencias de datos interables y los ordena en relación clave:valor
#Las secuencias deben tener el mismo numero de elementos

var_diccionario = dict(zip(["Uno", "Dos", "Tres", "cuatro"], [1,2,3,4]))
"""uno = "uno"
dos = "dos"
dic = dict(zip((uno, dos), [1,2]))"""

print(var_diccionario)

#items -> mediante un diccionario y devolver una lista de tuplas
var_items = var_diccionario.items()
print(var_items)

#keys -> Regresarme una lista que contiene las llaves del diccionario
var_keys = {"numero":20, "vocal":'a'}.keys()
print(var_keys)

#values -> mediante un diccionario crea una lista con los valores
var_values = {"numero":20, "vocal":'a'}.values()
print(var_values)

#clear -> Eliminar todos los items (parejas) que hay en el diccionario
diccionario_dario = {"nombre":"Frost", "nacionalidad":"Canadá"}
print(diccionario_dario)
diccionario_dario.clear()
print(diccionario_dario)

#copy -> Clonar el diccionario
original = {"nombre":"Frost", "nacionalidad":"Canadá"}
copia = original.copy()


"""
diccionario_dario = {"nombre":"Frost", "nacionalidad":"Canadá"}
diccionario_duplicado = diccionario_dario
print(diccionario_duplicado)
diccionario_duplicado['nombre'] = "Kaid"
print(diccionario_duplicado)
print(diccionario_dario)

lista1 = [1,2,3]
lista2 = lista1
lista2[0] = 700

print(lista1)
print(lista2)

def fun():
    #sas
    pass

print(fun)
"""

#Recibe una coleccion de datos que usará como clave y a todos les asigna como valor el argumento
#brindado

var_dir = dict.fromkeys(["Estado", "Activo"], True)
print(var_dir)

#get -> Recuperar un valor segun una clave
var_dir['Estado']
valor = var_dir.get('Estado')
print(valor)

#pop -> Devuelve un elemento y lo elimina de la estructura, si no lo encuentra da error
animales = \
{"felinos":["gato", "leon", "chita", "leopardo"],
 "aves":["tucan", "cuervo"],
 "aves2":["tucan", "cuervo"]
}
print(animales)
animales.pop('aves2')
print(animales)

#setdefault
#1st -> como metodo get
tonchis = animales.setdefault('felinos')
print(tonchis)
#2nd -> para agregar un nuevo elemento al diccionario
animales.setdefault('reptiles',["Iguana", "Caiman", "Cocodrilo", "Python"])
print(animales)

#update -> Actualiza un diccionario a partir de otro

alfabeto = {}
vocales = {"A":'A', "E":'E', "I":'I', "O":'O', "U":'U'}
letras = {"A":'A', "E":'E', "I":'I', "O":'O', "U":'U', "X":'X', "Z":'Z'}

alfabeto.update(vocales)
print(alfabeto)
alfabeto.update(letras)
print(alfabeto)
letras = {"A":'A', "E":'E', "I":'I', "O":'O', "U":'U', "X":'x', "Z":'z'}
alfabeto.update(letras)
print(alfabeto)