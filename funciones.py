#Una funcion es un bloloque de codigo reutilizable se encarga de una determinada tarea

#Modular nuestra aplicacion, segmentar modulos mas simples nuestro codigo
#Reutilzables, permite utilizar unja misma funcion en distintos programas
#Nos brindan soluciones generales
def mi_funcion():
    return "Hola Mundo"
    
#print(mi_funcion())
#NameSpace -> Sistema que permite gestionar los nombres de mis variables y funciones
#Rule LGEB

def externa():
    def interna():
        print(var)
    interna()
externa()



