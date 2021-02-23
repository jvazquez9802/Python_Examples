import math

figuras = []
figuras.append({"tipo":"Cuadrado", "area":16, "perimetro":16})
figuras.append({"tipo":"Cuadrado", "area":4, "perimetro":8})
figuras.append({"tipo":"Triangulo Escaleno", "area":12.23, "perimetro":9})
figuras.append({"tipo":"Triangulo Equilatero", "area":25, "perimetro":56})
figuras.append({"tipo":"Triangulo Isosceles", "area":25, "perimetro":58})
figuras.append({"tipo":"Circulo", "area":24, "perimetro":36})

def separar_clasificacion():
    circulos = []
    t_equilateros = []
    t_isosceles = []
    t_escalenos = []
    cuadrados = []
    
    for i in figuras:
        if i.get('tipo').lower() == "cuadrado":
            cuadrados.append(i)
        elif i.get('tipo').lower() == "circulo":
            circulos.append(i)
        else:
            if i.get('tipo').lower() == "triangulo equilatero":
                t_equilateros.append(i)
            elif i.get('tipo').lower() == "triangulo isosceles":
                t_isosceles.append(i)
            else:
                t_escalenos.append(i)
    return [cuadrados, circulos, t_equilateros, t_isosceles, t_escalenos]


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
                        print(imprimir_figura(i))
                
                if not bandera:
                    print("No hay elementos para esta clasificación aún")
                        
        elif clasificacion.lower() == "cuadrado" or clasificacion.lower() == "circulo":
            for i in figuras:
                    if clasificacion.lower() == i.get('tipo').lower():
                        bandera = True
                        print(imprimir_figura(i))
            if not bandera:
                    print("No hay elementos para esta clasificación aún")
        else:
            print("[ERROR] Tipo de Figura no válido")
            

    def imprimir():
        
        clasificaciones = separar_clasificacion()
        
        def imprimir_clasificacion(clasificacion, lista):
            print(f"===== {clasificacion} =====")
            for i in lista:
                print(imprimir_figura(i))
            print()
            
        for i in clasificaciones:
            imprimir_clasificacion(i[0].get('tipo').upper(), i)
    
    
    def sumador_propiedad(propiedad):
        print(f"==== {propiedad.upper()} POR CLASIFICACION ====")
        clasificaciones = separar_clasificacion()
        for i in clasificaciones:
            sumador = 0
            print(f" -> {i[0].get('tipo').upper()}", end="")
            for j in i:
                sumador += j.get(propiedad)
            print(f" {sumador}")
    
    while True:
        print("============ Menu Figuras ============\n1.- Crear Figura\n2.- Listar Clasificación\n"\
            +"3.- Listar Todo\n4.- Suma de áreas\n5.- Suma de perímetros\n6.- Limpiar Lista\n0.- Salir")
        op = input("Selecciona una opción [0 : 6] ->  ")
        if op == "1":
            menu_figuras()
        elif op == "2":
            listar_clasificacion(input("Ingresa la clasificación a imprimir -> "))
        elif op == "3":
            imprimir()
        elif op == "4":
           sumador_propiedad("area")
        elif op == "5":
           sumador_propiedad("perimetro")
        elif op == "6":
            figuras.clear()
            print(f"Se han eliminado todos los registros: {figuras}")
        elif op == "0":
            print("Gracias por utilizar nuestra calculadora... [Saliendo]")
            return
        else:
            print(f"[WARNING] -> {op} <- No es una opción válida, intenta de nuevo.")

main()