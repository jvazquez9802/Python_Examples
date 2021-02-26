#Iterados

#iter() __iter__()  => Devuelve un objeto iterable
#

#xrange()

lista = [1,2,3,4,5,6]

objeto_iterable = iter(lista) #Iter de izquierda a derecha
#objeto_iterable = reversed(lista) de derecha a izquierda

#lista.__iter__()

while True:
    try:
        print(next(objeto_iterable))
        #objeto_iterable.__next__()
    except StopIteration:
        print("Ya no hay nada para mostrar")
        break

