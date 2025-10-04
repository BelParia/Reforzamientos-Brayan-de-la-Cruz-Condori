# Reforzamiento 5

## Clases

### Ejercicio 7, en el documento no sigue el orden adecuado
"""
Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase Persona
y agregue un atributo sueldo. Crearás un método que indicará si debe pagar
impuestos (que sería el 10% de su sueldo y si sueldo es superior a 4000 soles)
Instanciar la clase Empleado al menos para 3 empleados, mostrar el sueldo
del empleado y cuánto debe pagar de impuesto.
"""

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad (en años): "))

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo (en S/): "))

    def calcular_impuesto(self):
        if self.sueldo > 4000:
            impuesto = self.sueldo * 0.10
            print(f"{self.nombre} debe pagar S/ {impuesto:.2f} de impuesto (10% de su sueldo). Pucha, terrible los impuestos")
        else:
            print(f"{self.nombre} no paga impuesto porque su sueldo es S/ {self.sueldo:.2f}. Felicidades !!!")

empleado1 = Empleado()
empleado1.calcular_impuesto()

empleado2 = Empleado()
empleado2.calcular_impuesto()

empleado3 = Empleado()
empleado3.calcular_impuesto()