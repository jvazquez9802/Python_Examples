from Figura import Figura as F

class Cuadrado(F):

    def __init__(self, lado):
        super().__init__()
        self.lado = lado
    
    def calcular_area(self):
        self.area = self.lado ** 2
        
    def calcular_perimetro(self):
        self.perimetro = self.lado * 4
    