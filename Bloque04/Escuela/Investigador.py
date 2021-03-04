from Persona import Persona

class Investigador(Persona):
    def __init__(self, nombre, fecha_n, genero, departamento):
        super().__init__(nombre, fecha_n, genero)
        self.departamento = departamento
