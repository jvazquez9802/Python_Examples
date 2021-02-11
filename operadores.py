#OPERADORES ARITMETICOS

suma = 8 + 20
resta = 8 - 5
negacion = -20
multi = 8 * 20
potencia = 8 ** 20
division = 4 / 2
division_entera = 8 // 20
modulo = 8 % 20
frase = "Mundo"

cadena = "Hola " + frase + \
    ("!" * int(division) ** resta)
    
#LOGICOS

#True and True = True
#True and False = False
#False and True = False
#False and False = False

numero = 3
if 2 == numero and numero == 2:
    print("Verdad")
    
numero = 2
if 3 == numero or numero == 3:
    pass
    
#True or True = True
#True or False = True
#False or True = True
#False or False = False

booleano = True
if not booleano:
    print("Verdad")

#Relacionales

a, b, c = 32, 32, 20
# Igual que ==

if not(c > a or a != b+2):
    print("Evaluando multiples premisas")
    
if a == b:
    print("Son iguales")
    
if a != b:
    print("Son diferentes")
    
if a >= b:
    print(str(a) + "es mayor o igual que " + str(b))
    
if a <= b:
     print(str(a) + "es menor o igual que " + str(b))

if a > b:
    print(str(a) + "es mayor que " + str(b))

if a < b:
    print(str(a) + "es menor " + str(b))
    
#Operador Ternario
resultado="Mayor que cero" if 20>0 else "Menor o igual que cero"
print(resultado)

#Asignación
variable, var1 = 3, 4
var2 = var3 = 0

variable += 2
variable -= 2
variable *= 2
variable /= 2
variable **= 2
variable //= 2
variable %= 2



