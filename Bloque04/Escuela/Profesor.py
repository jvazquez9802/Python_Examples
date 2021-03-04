from Persona import Persona

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
           