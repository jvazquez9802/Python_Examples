#Una clase para Profesor, investigador, Persona, Profesor Universitario

#Herencia me representa una relacion entre clases, permitiendo a su vez crear clases especializadas

class Persona():
    def __init__(self, nombre, fecha_n, genero):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_n
        self.genero = genero
        
    def login(self):
        print(f"{self.nombre} inició sesión")
        
    def logout(self):
        print(f"{self.nombre} cerró sesión")

class Profesor(Persona):
    def __init__(self, nombre, fecha_n, genero, cedula):
        super().__init__(nombre, fecha_n, genero)
        self.cedula = cedula
        self.especialidad = None
    def __str__(self):
        if self.especialidad:
            return """ %s nació en %s con cedula %s especializado en %s""" % (self.nombre, self.fecha_nacimiento, self.cedula, self.especialidad.nombre)
        else:
            return """ %s nació en %s con cedula %s""" % (self.nombre, self.fecha_nacimiento, self.cedula)
            
class Investigador(Persona):
    def __init__(self, nombre, fecha_n, genero, departamento):
        super().__init__(nombre, fecha_n, genero)
        self.departamento = departamento


objeto = Persona("Juan", "20/02/1998", "M")
print(objeto.nombre)
objeto.login()

print(objeto)

objeto1 = Profesor("Adriana", "25/02/1988", "F", "XXX000XX0")
print(objeto1)

print()

objeto2 = Investigador("Felipe", "03/01/1995", "M", "Ciencias Básicas")
print(objeto2.departamento)
objeto2.login()

print()



"""class ProfesorUniversitario(Profesor, Investigador):
    def __init__(self, nombre, fecha_n, genero, cedula, departamento, turno):
        Profesor.__init__(self, nombre, fecha_n, genero, cedula)
        Investigador.__init__(self, nombre, fecha_n, genero, departamento)
        self.turno = turno
        


objeto3 = ProfesorUniversitario("Matilda", "26/04/2001", "M","ZZZ111ZZ1", "Ciencias Computacionales", "Matutino", "")
print(objeto3)"""


