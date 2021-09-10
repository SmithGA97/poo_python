class Circulo:
    
    __pi = 3.141592
    
    def __init__(self, radio):
        self.__radio = radio
    
    def __cuadrado(self, n):
        return n ** 2
    
    def area(self):
        return Circulo.__pi * self.__cuadrado(self.__radio)
    
    def valorRadio(self):
        return self.__radio
    
    def fijaRadio(self, nuevoRadio):
        self.__radio = nuevoRadio

c = Circulo(3)
print(c.area())
print(c.valorRadio())
c.fijaRadio(4)
print(c.valorRadio())
print(c.area())
#intentando modificar el radio para que cambiar areea
c.__radio=10
print(c.area())
