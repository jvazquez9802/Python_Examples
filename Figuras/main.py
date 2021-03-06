from pickle import dump, dumps, load, loads, Unpickler
from utilidades import menu_principal
from Figura import Figura


data=[]

def cargar():
    with open("bd.bin", "rb") as fl:
        try:
            global data
            data = list(load(fl))
        except EOFError:
            data = []
            
    print(data)
    

def guardar():
    with open("bd.bin", "wb") as fl:
        dump(data, fl)
        

def main():
    menu_principal(data)



if __name__ == '__main__':
    cargar()
    main()
    guardar()