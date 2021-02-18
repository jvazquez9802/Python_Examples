#Se ejecuta mientras un criterio sea verdadero

bandera = False
numero = 1

while bandera:
    print(numero)
    numero+=1
    
op = ""

while op != "0":
    print("1.- Menu 1\n2.- Menu 2\n0.- Salir")
    op = input("Ingresa una opcion")


"""    if(op == "0"):
        break
else:
    print("Puedo tener un else")"""