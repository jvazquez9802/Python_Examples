from Cuadrado import Cuadrado
from Circulo import Circulo
from Triangulo import Triangulo

def menu_secundario(lista):
     while True:
        print("MENU SECUNDARIO".center(30, "=") + "\n1.-Cuadrado\n2.-Circulo\n3.-Triangulo\n0.-Volver al menú principal")
        op = input("Elige una opción [0:3]")
        if op == "1":
            nuevo = Cuadrado(float(input("Lado: ")))
            nuevo.calcular_area()
            nuevo.calcular_perimetro()
            lista.append(nuevo)
        elif op == "2":
            nuevo = Circulo(float(input("Radio: ")))
            nuevo.calcular_area()
            nuevo.calcular_perimetro()
            lista.append(nuevo)  
        elif op == "3":

            nuevo = Triangulo(float(input("Lado A: ")), float(input("Lado B: ")), float(input("Lado C: ")))
            nuevo.calcular_area()
            nuevo.calcular_perimetro()
            lista.append(nuevo)  
        elif op == "0":
            print("Saliendo...")
            return
        else:
            print(f"El valor [ {op} ]: No es una opcion valida, prueba de nuevo")

def menu_principal(lista):
    while True:
        print("MENU PRINCIPAL".center(30, "=") + "\n1.-Crear Figura\n2.-Listar Figuras\n3.-Sumar Areas\n4.-Sumar Perimetros\n0.-Salir")
        op = input("Elige una opción [0:4]")
        if op == "1":
            menu_secundario(lista)
        elif op == "2":
            count = 1
            for obj in lista:
                print(f"id: {count} Tipo: {obj.__class__.__name__} Area: {obj.area} Perimetro: {obj.perimetro}")
                count += 1
                
        elif op == "3":
            area = 0.0
            for obj in lista:
                print(area)
                area += obj.area
            print(f"La suma de areas es: {area}")
            
        elif op == "4":
            perimetro = 0.0
            for obj in lista:
                perimetro += obj.perimetro
            print(f"La suma de perimetros es: {perimetro}")
        elif op == "0":
            print("Saliendo...")
            return
        else:
            print(f"El valor [ {op} ]: No es una opcion valida, prueba de nuevo")