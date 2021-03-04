import Profesor
from Investigador import Investigador as I
from utilidades import imprimir_registro

def main():
    
    registros = []
    
    while True:
        print(f"1.- Registrar profesor\n2.- Registrar Investigador\n3.-Listar Registros\n0.-Salir\n")
        op = int(input("Elige una opcion [0:2]"))
        if op == 1:
            registros.append(Profesor.Profesor(input("Nombre: "), input("Fecha: "), input("Genero"), input("Cedula")))
        elif op == 2:
             registros.append(I(input("Nombre: "), input("Fecha: "), input("Genero"), input("Turno")))
        elif op == 3:
            for r in registros:
                imprimir_registro(r)
        elif op == 0:
            print("Saliendo")
        else:
            break
        

if __name__ == "__main__":
    main()