class Persona():
    def __init__(self, nombre, fecha_n, genero):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_n
        self.genero = genero
        
    def login(self):
        print(f"{self.nombre} inició sesión")
        
    def logout(self):
        print(f"{self.nombre} cerró sesión")