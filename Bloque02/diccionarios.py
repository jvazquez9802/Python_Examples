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