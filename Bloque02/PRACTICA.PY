import math

figuras = []


def area_cuadrado(lado):
    return lado ** 2


def area_circulo(radio):
    return math.pi * radio ** 2


def area_triangulo(lado_a, lado_b, lado_c):
    altura = 0.0
    if lado_a == lado_b and lado_b == lado_c:
        #Equilatero
        altura = (math.sqrt(3) * lado_a)/2
    else:
        if lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
            #Isósceles
            if lado_a == lado_b:
                altura = math.sqrt(((lado_a ** 2) - (lado_c **2))/4)
            elif lado_a == lado_c:
                altura = math.sqrt(((lado_a ** 2) - (lado_b **2))/4)
            else:
                altura = math.sqrt(((lado_b ** 2) - (lado_a **2))/4)
                
            return ("Triangulo Isósceles", (lado_b * altura)/2)
        else:
            semi_p = (lado_a + lado_b + lado_c)/2
            return ("Triangulo Escaleno", math.sqrt(semi_p * (semi_p - lado_a) * (semi_p-lado_b) * (semi_p - lado_c)))
    return ("Triangulo Equilatero", (lado_b * altura)/2)
        
    
def perimetro_cuadrado(lado):
    return lado * 4


def perimetro_circulo(radio):
    return 2 * math.pi * radio


def perimetro_triangulo(lado_a, lado_b, lado_c):
    return lado_a + lado_b + lado_c


def main():
    
    def imprimir_figura(dic):
        return(f"Tipo: {dic.get('tipo')} área: {dic.get('area')} perimetro: {dic.get('perimetro')}")
    
    def menu_figuras():
        
        
        def crear_cuadrado(lado):
            diccionario = {"tipo":"Cuadrado", "area":area_cuadrado(lado), "perimetro":perimetro_cuadrado(lado)}
            figuras.append(diccionario)
            print(f"Figura creada -> {imprimir_figura(diccionario)}")
            
            
        def crear_triangulo(lado_a, lado_b, lado_c):
            propiedades = area_triangulo(lado_a, lado_b, lado_c)
            diccionario = {"tipo":propiedades[0], "area":propiedades[1], "perimetro":perimetro_triangulo(lado_a, lado_b, lado_c)}
            figuras.append(diccionario)
            print(f"Figura creada -> {imprimir_figura(diccionario)}")
            
            
        def crear_circulo(radio):
            diccionario = {"tipo":"Circulo", "area":area_circulo(radio), "perimetro":perimetro_circulo(radio)}
            figuras.append(diccionario)
            print(f"Figura creada -> {imprimir_figura(diccionario)}")
            
        
        
        while True:
            print("============ Crear Figura ============\n1.- Cuadrado\n2.- Triángulo\n3.- Círculo\n0.- Cancelar")
            op = input("Selecciona una opción [1 : 3] ->  ")
            if op == "1":
                crear_cuadrado(float(input("Ingresa la medida de los lados -> ")))
            elif op == "2":
                lado_a = float(input("Ingresa el lado A: "))
                lado_b = float(input("Ingresa el lado B: "))
                lado_c = float(input("Ingresa el lado C: "))
                crear_triangulo(lado_a, lado_b, lado_c)
            elif op == "3":
                crear_circulo(float(input("Ingresa la medida del radio -> ")))
            elif op == "0":
                print("Regresando al menú principal... [Cancelado]")
                return
            else:
                print(f"[WARNING] -> {op} <- No es una opción válida, intenta de nuevo.")
                
    
    def listar_clasificacion(clasificacion):
        
        bandera = False
        
        if clasificacion.lower() == "triangulo":
            var = input("Ingresa el tipo de triangulo que quieras buscar [equilatero; isosceles; escaleno]")
            if var.lower() != "equilatero" and var.lower() != "isosceles" and var.lower() != "escaleno":
                print("[ERROR] Tipo de triágulo no válido")
            else:
                var = clasificacion + " " + var
                for i in figuras:
                    if var.lower() == i.get('tipo').lower():
                        bandera = True
                        imprimir_figura(i)
                
                if not bandera:
                    print("No hay elementos para esta clasificación aún")
                        
        elif clasificacion.lower() == "cuadrado" or clasificacion.lower() == "circulo":
            for i in figuras:
                    if clasificacion.lower() == i.get('tipo').lower():
                        bandera = True
                        imprimir_figura(i)
            if not bandera:
                    print("No hay elementos para esta clasificación aún")
        else:
            print("[ERROR] Tipo de Figura no válida")
            
            
        
    
    
    while True:
        print("============ Menu Figuras ============\n1.- Crear Figura\n2.- Listar Clasificación\n"\
            +"3.- Listar Todo\n4.- Suma de áreas\n5.- Suma de perímetros\n6.- Limpiar Lista\n0.- Salir")
        op = input("Selecciona una opción [0 : 6] ->  ")
        if op == "1":
            print(figuras)
            menu_figuras()
        elif op == "2":
            listar_clasificacion(input("Ingresa la clasificación a imprimir -> "))
        elif op == "3":
            print("Soy la opcion 3")
        elif op == "4":
            print("Soy la opcion 4")
        elif op == "5":
            print("Soy la opcion 5")
        elif op == "6":
            print("Soy la opcion 6")
        elif op == "0":
            print("Gracias por utilizar nuestra calculadora... [Saliendo]")
            return
        else:
            print(f"[WARNING] -> {op} <- No es una opción válida, intenta de nuevo.")

main()