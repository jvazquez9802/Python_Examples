from Figura import Figura as F
import math

class Triangulo(F):

    def __init__(self, lado_a, lado_b, lado_c):
        super().__init__()
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
    
    def calcular_area(self):
        semi_p = (self.lado_a + self.lado_b + self.lado_c)/2
        self.area = math.sqrt(semi_p * (semi_p - self.lado_a) + \
            semi_p * (semi_p - self.lado_b) + semi_p * (semi_p - self.lado_c) )
        
    def calcular_perimetro(self):
        self.perimetro = self.lado_a + self.lado_b + self.lado_c
    