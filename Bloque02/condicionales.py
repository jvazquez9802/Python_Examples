#Condiciones
#if elif else
#Permiten condicionar las ejecución de uno o varios bloques de sentencias al cumplimiento
#de una premisa

#Simples
n1 = 2
n2 = 9

if not(n1 <= n2 and n1 > 0): #Falso
    print(f"{n1} si es igual a {n2}")

print('Continuamos con el flujo normal, fin de la ejecución')


#Si el resultado de la evaluacion es:
#True el bloque de sentencias SI se ejecuta
#False el bloque de sentencias NO se ejecuta

#dobles
letra = 'a'
vocales = ('a','e','i','o','u')

if letra in vocales:
    print(f"la letra {letra} es una vocal")
else:
    print(f"la letra {letra} no es una vocal")
    
#anidadas
#Saber si un numero es par o inpar (Solo evaluar numeros positivo)
"""numero = input("Ingresa un número")
if int(numero) >= 0:
    if int(numero) % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es inpar")
else:
    print("El numero no se evaluó porque es negativo")"""

#Multiples
#Saber si un numero es par o inpar (Solo evaluar numeros positivo)
#Si el numero es negativo mostramos su valor absoluto
#Excluir al 0 de los positivos y decir que ingrese algo diferente

numero = int(input("Ingresa un número"))
if numero > 0:
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
elif numero < 0:
    print(f"El numero es negativo ({ numero }) su valor absoluto es: {abs(numero)}")
else:
    print("Ingresaste un cero, prueba con otro numero")



    

