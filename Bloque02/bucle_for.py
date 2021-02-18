#Bucle For ejecuta un bloque de codigo mientras se cumple una condicion
#Ejecutarse un numero determinado de veces

#OBJETOS ITERABLES
#Listas
#Tuplas
#Cadenas de caracteres
#Diccionarios
#Rangos

#for(int e:items){
#    
#}

for i in [0,10,20,30,50]:
    print(f"La variable i vale {i}", end=" ")
    
for i in []:
    print(i)

print()

for i in (24, "Un Texto"):
    print("i vale " + str(i))

oficios = ["Carpintería", "Herrería", "Sastrería"]

for i in range(len(oficios)):
    print(f"En el indice {i} se encuentra {oficios[i]}")

dic = dict(zip(["Uno", "Dos", "Tres", "cuatro"], range(1,5)))

for k,v in dic.items():
    print(f"Para la clave {k} su valor es {v}")
    
print(dic)
print(dic.keys())
for key in dic.keys():
    print(f"para {key} es {dic.get(key)}")
    
letras = ('a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h')
obj_slice = slice(3,5)
print(f"Slice {obj_slice}")
print(letras[obj_slice])

for i in letras[2:4:2]:
    print(f"Usando a slice {i}")
    
for l in "WandaVision"[-1:-5:-1]:
    print(l + " ", end="\b")
    
print()    

# recorrer un objeto iterable definiendo un inicio y un fin para el recorrido
#Igualmente puedo definir 

"""
nombres = []
for var in range(int(input("Cuantos nombres agregarás"))):
    nombres.append(input(f"Agrega el registro {var}"))
    
print(nombres)
"""

numeros = list(range(7))

#CONTINUE pasa a la siguiente iteracion del bucle e ignora el resto de sentencias
for par in numeros:
    if par%2 != 0:
        continue
    print(par, end=" ")
    print(f"{par} no me ignora")
    
for i in range(6):
    #Porque quiero y puedo
    pass


for i in "17460654tecnm.colima.mx":
    if i == "@":
        print("Hay un arroba, bien")
        break
else:
    print("No hay un arroba, mal")
    
