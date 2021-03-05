#texto
#CSV
#XML
#JSON
#Binarios

#PROCEDIMIENTO

#1.- Abrir el archivo
#2.- Se lee o se escribe en el archivo
#3.- Se cierra el archivo

#Un archivo de texto está formado por cadenas de caracteres sin ningun formato y estos son legibles para 
#personas

#Leer
"""
archivo_texto = open("texto.txt", "r") #read
print(archivo_texto.read())
archivo_texto.close()

archivo_texto = open("texto.txt", "r") #read
for linea in archivo_texto.readlines():
    for caracter in linea:
        if caracter.isupper():
            print(caracter)
archivo_texto.close()

"""

#Escribir
"""archivo_texto = open("texto.txt", "r") #read
print(archivo_texto.read())
archivo_texto.close()

print()"""
"""
archivo_texto = open("texto.txt", "w") #w sobre escribe el archivo
archivo_texto.write("Aaaahnocheto, me gusta lo que hago... creo")
archivo_texto.close()

"""

"""archivo_texto = open("texto.txt", "a") #w sobre escribe el archivo
archivo_texto.write("\nAaaahnocheto, me gusta lo que hago... creo")
archivo_texto.close()
"""

#Lo idea es manejar errores en tiempo de ejecución
"""
try:
    archivo_texto = open("texto.txt", "a") #read
except Exception:
    print("Algo salió mal, pa'casa chaval")
else:
    archivo_texto.write("Aaaahnocheto, me gusta lo que hago... creo")
finally:
    archivo_texto.close()



with open("texto.txt", "r+") as fl:
    try:
        fl.write("Soy otra linea")
    except Exception:
        print("Algo va mal")
"""

"""with open("calculo.csv", "w") as fl:
    try:
        fl.write("Datos, Datoss, Datosss")
    except Exception:
        print("Algo va mal")
"""

datos = []
with open("calculo.csv", "r") as fl:
    try:
        for i in fl.readlines():
            print(i)
            datos.append(i.rstrip('\n').split(","))
    except Exception:
        print("Algo va mal")

print(datos)