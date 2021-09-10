class Circulo:
    
    pi = 3.141592
    
    def __init__(self, radio):
        self.radio = radio
    
    def cuadrado(self, n):
        return n ** 2
    
    def area(self):
        return Circulo.pi * self.cuadrado(self.radio)
    
    def valorRadio(self):
        return self.radio
    
    def fijaRadio(self, nuevoRadio):
        self.radio = nuevoRadio

c = Circulo(3)
print(c.area())
print(c.valorRadio())
c.fijaRadio(4)
print(c.valorRadio())
print(c.area())
#intentando modificar el radio para que cambiar areea
c.radio=10
print(c.area())