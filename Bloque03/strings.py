#CADENAS DE CARACTERES a profundidad

# Tipos de datos compuestos que pertenecen a la clase str
#Atributos/Propiedades/Características propias del tipo de objeto
#Metodos/Procedimientos/acciones

#Analisis -> Analizar el contenido de la cadena

txt = " Hola\tMundo! "
print(txt)
#Count => Conocer el número de veces que se encuentra un elemento en la cadena
print(f'Count: {txt.count("Hola")}')

#Retornan la pocisión en la que se encuentra el elemento iniciando desde 0
    #find
print(f"Find: {txt.find('a')}") #No encontrado regresa -1

"""if txt.index('z') == -1:
    print('No encontrado')"""
    #index
print(f"Index: {txt.index('o')}") #No encontrado regresa ValueError

print(f"Derecha Find: {txt.rfind('a')}") #No encontrado regresa -1
    #index
print(f"Derecha Index: {txt.rindex('o')}") #No encontrado regresa ValueError

ss1 = " Hola"
ss2 = "Mundo"

#startswith retorna un valor bool si la cadena en cuestion comienza con el argumento que se recibe
print(f"Comienza con {ss1}? => {txt.startswith(ss1)}")
#print(txt[:len(ss1)] == ss1)

#endswith retorna un valor bool si la cadena en cuestion termina con el argumento que se recibe
print(f"Termina con {ss2}? => {txt.endswith(ss2)}")

#Se utilizan para determinar si todos los caracteres que contiene la cade son digitos, numeros o numeros con decimales
    #isdigit
numeros = "102av0"
print(f"Digito: {numeros.isdigit()}") #Evaluan caracteres que pueden formar numeros incluyendo caracteres de lenguas orientales
    #isdecimal
print(f"Decimal: {numeros.isdecimal()}") #Evalua caracteres que pertenece 0-9
    #isnumeric
print(f"Numerico: {numeros.isnumeric()}")#Evalua fracciones

print(f"isalnum: {'123♠abc'.isalnum()}")#Evalua si los caracteres son letras o numeros
print(f"isalpha: {'abc'.isalpha()}")#Evalua si los caracteres se encuentran dentro del alfabeto
print(f"islower: {'hola'.islower()}")#Evalua si los caracteres son minusculas
print(f"isupper: {'Hola'.isupper()}")#Evalua si los caracteres son mayusculas
print(f"isprintable: {' Hola    Mundo! '.isprintable()}")#Evalua son imprimibles
print(f"isspace: {'     '.isspace()}")#Evalua si son espacios

#"Transformación"
#Las cadenas en Python no son mutables entonces se crea un nuevo objeto
#Capitalize
print(f"Capitalizar: {'en el año...'.capitalize()}")
#encode
print(f"Codificar: {'hola'.encode('utf-8')} bytes {bin(5)}" ) #Regresa una instancia de bytes
#Alinea un cadena conforme una cantidad de caracteres
#Centrar
print(f"centrar: {'Titulo'.center(10,'*')}")
#alinear derecha
print(f"derecha: {'Titulo'.rjust(10)}")
#alinear izquierda
print(f"izquierda: {'Titulo'.ljust(10)}")
#alinear lower 
print(f"Minúscula: {'Soy Un Titulo'.lower()}") #
#alinear upper
print(f"Mayúsculas: {'Soy Un Titulo'.upper()}")
#alinear swapcase
print(f"izquierda: {'Soy Un Titulo'.swapcase()}") 
#alinear strip

print(f"Elimar espacios: {' eliminar '.strip()}")
#alinear lstrip
print(f"Elimar espacios izquierda: {' Soy Un Titulo   '.lstrip()}")
#alinear rstrip
print(f"Elimar espacios derecha: {'   Soy Un Titulo '.rstrip()}")
#alinear replace
print(f"Reemplazar: {'   Soy Un Titulo   '.lower().replace('titulo','parrafo')}")



#Separación y unión
print(f'{"Separación y unión".center(40,"*")}')

#split
text= 'Hola Mundo\nQue onda'
print(f"Split: {text.split()}") #Divide una cadena de caracteres en una lista segun un caracter especificado
#Por defecto es el espacio y salto de linea
print(f"Split solo saltos de linea: {text.splitlines()}")
#Separar indicando maximo de separaciones
text = "uno,dos,tres,cuatro"
print(f"Split con maximo: {text.split(',', -1)}") #Un -1 indica separaciones ilimitadas
text = text= 'Hola Mundo\nQue onda'
print(f"partir en una tupla de 3: {text.partition('Mundo')}") #(antes sep, sep, despues sep)
text = text= 'Hola Juan\nQue onda Juan amigo'
print(f"Split con maximo: {text.rpartition('Juan')}")
#Join
print(f"Join: {'Dice: '.join(['Buenas','Nuevas'])}") #Une cadenas de caracteres mediante una cadena especificada
