# Reforzamiento 5

## Clases

### Ejercicio 5, en el documento no sigue el orden adecuado
"""
Crear una clase PersonaPrestamo que hereda de la clase anterior
(problema 5) donde tendrá los métodos: Uno, que indicará si la persona está
apta para un préstamo solo si ha estado más de 12 meses trabajando en la
empresa en caso contrario se le informa que no es posible darle el préstamo
y la otra condición adicional es si su edad es mayor de 25 años.
Agregar un segundo métod0 a esta nueva clase que te indicará si estás
aprobado recibirás 10 veces tu sueldo de préstamo, el total de préstamo
otorgado es {cantidad_prestamo}.
Instanciar 3 veces la clase para mostrar diferentes resultados.
"""

from R5_Clases_4 import Persona

class PersonaPrestamo(Persona):
    def __init__(self, nombre, edad, sueldo, meses_trabajados):
        super().__init__(nombre, edad, sueldo, meses_trabajados)

    def evaluar_prestamo(self):
        if self.meses_trabajados > 12 and self.edad > 25:
            print(f"{self.nombre} está apto para solicitar un préstamo. Felicidades !!!")
            return True
        else:
            print(f"{self.nombre} no cumple los requisitos para el préstamo. Tranquilo (a), la siguente será...")
            return False

    def calcular_prestamo(self):
        if self.evaluar_prestamo():
            cantidad_prestamo = self.sueldo * 10
            print(f"Préstamo aprobado: ${cantidad_prestamo}")
        else:
            print("Préstamo no aprobado.")

persona1 = PersonaPrestamo("Brayan", 25, 1500, 26)
persona2 = PersonaPrestamo("Mirian", 17, 900, 8)
persona3 = PersonaPrestamo("Roly", 30, 2000, 48)

persona1.mostrar_datos()
persona1.calcular_prestamo()
print()

persona2.mostrar_datos()
persona2.calcular_prestamo()
print()

persona3.mostrar_datos()
persona3.calcular_prestamo()

