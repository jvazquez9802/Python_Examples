#excepciones 

while True:
    try:
        num = int(input("Ingresa un numero"))
        num = 1 / num
        print(num + num2)
        break
    except ValueError:
        print("Valor ingresado no admitido")
    except NameError:
        print("Tienes una variable no definida")
    except ZeroDivisionError:
        print("Tiende a infinito")

        

numero = 8
numero2 = 2
try:
    resultado = numero / numero2
except ZeroDivisionError:
    print("Tiende a infinito")
else:
    print(f"El resultado es: {resultado}")
    
    
try:
    print(hola)
except NameError as err:
    print(err)

try:
    raise NameError('Hola tienes un error')
except NameError:
    print("Autosabotaje")
    
#relanzando la excepcion

try:
    raise NameError('Hola tienes un error')
except NameError:
    print("Autosabotaje")
    raise
    


def funcion():
    raise IOError

try:
    funcion()
except IOError as exc:
    raise RuntimeError("Algo ocurrio mal en la lectura") from exc



#Primero se ejecuta la clausula try (try y except son palabras reservadas)
#Si NO ocurre algún error en las instrucciones anidadas a la clausula try, la clausula except se omite
#Si ocurre algun error el resto de las instrucciones en la clausula try se omiten
#Si el error coincide con la clausula except se ejecutan las instrucciones indicadas
#Si el erro no coincide con la clausula except se toma como una excepcion no manejada/ gestionada y se interrumpe la ejecución

#Acciones de limpieza clausula finally

def verdad_falsedad():
    n = 8
    try:
        n /= 2
    except ZeroDivisionError:
        print("Infinito")
    else:
        print(n)
        return n
    finally:
        print('Yo me ejecuto siempre')


print(verdad_falsedad())


try:
    file = open('file.txt')
except Exception:
    print("Algo salio mal")
else:
    for line in file:
        print(line.strip())
finally:
    file.close()
    


""" PENDIENTE EXCEPT COMO COMODIN

CREACION DE PROPIAS EXCEPCIONES

except:
    print("Error inesperado")
    raise"""