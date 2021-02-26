#Los generadores son funciones especiales que puede realizar procedimientos y retornar valores con
#ls instruccion yield

#Cada vez que se llame a este tipo de funcion, se reanuda desde el punto en el que se quedó

def generador_pares(stop): #Puedo recibir argumentos
    contador = 1
    while contador < stop:
        yield contador
        yield contador * 2
        contador += 1
    
#con return nosotros podemos detener al generador (OJO: Maneja la excepcion)
        
#Generar los numeros pares del 0 al 100
generador = generador_pares(3)
"""
variable_generada = 0
while variable_generada < 100:
    variable_generada = next(generador)
    print(variable_generada)"""
    
print(f"Contador: {next(generador)} nPar: {next(generador)}")
print(f"Contador: {next(generador)} nPar: {next(generador)}")
print(f"Contador: {next(generador)} nPar: {next(generador)}")