# Reforzamiento 5

## Clases

### Ejercicio 2
"""
Crear una clase llamada Circulo que contenga radio en su constructor y
que contenga un métod0 área que devuelva el área de un círculo.
Adicionalmente habrá un métod0 que devuelva el perímetro del círculo.
También habrá un métod0 donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola
"""

import math

class Circulo:
    def __init__(self, radio=0):
        self.radio = radio

    def pedir_radio(self):
        self.radio = float(input("Ingrese el radio del círculo: "))

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

circulo1 = Circulo()
circulo1.pedir_radio()
print("Área:", circulo1.area())
print("Perímetro:", circulo1.perimetro())

circulo2 = Circulo()
circulo2.pedir_radio()
print("Área:", circulo2.area())
print("Perímetro:", circulo2.perimetro())

