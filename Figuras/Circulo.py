from Figura import Figura as F
import math

class Circulo(F):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
         
    def calcular_area(self):
        self.area = math.pi * (self.radio ** 2)
        
    def calcular_perimetro(self):
        self.perimetro = math.pi * self.radio * 2      
        