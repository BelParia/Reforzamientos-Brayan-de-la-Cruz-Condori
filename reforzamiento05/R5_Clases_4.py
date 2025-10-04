# Reforzamiento 5

## Clases

### Ejercicio 4, en el documento no sigue el orden adecuado
"""
Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una persona.
Implementar los métodos necesarios para inicializar los atributos
(constructor), un métod0 para mostrar los datos e indicar si la persona es
mayor de edad o no y otro métod0 que bonificación que retornará el 20%
adicional de su sueldo, en caso sea mayor de edad. Un métod0 para saber
cuántos meses ha estado trabajando en la empresa
Instanciar por lo menos la clase con 3 diferentes personas.
"""

class Persona:
    def __init__(self, nombre, edad, sueldo, meses_trabajados):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.meses_trabajados = meses_trabajados

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sueldo: {self.sueldo}")
        print(f"Meses trabajados: {self.meses_trabajados}")
        if self.edad >= 18:
            print("El empleado es mayor de edad")
        else:
            print("El empleado es menor de edad")

    def bonificacion(self):
        if self.edad >= 18:
            return self.sueldo * 1.20  # esto es el 20% adicional por ser mayor de edad
        else:
            return self.sueldo

    def tiempo_trabajo(self):
        anios = self.meses_trabajados // 12
        meses_restantes = self.meses_trabajados % 12
        print(f"Tiempo en la empresa: {anios} año(s) y {meses_restantes} mes(es)")

persona1 = Persona("Brayan", 25, 1500, 26)
persona2 = Persona("Mirian", 17, 900, 8)
persona3 = Persona("Roly", 30, 2000, 48)

persona1.mostrar_datos()
print("Sueldo con bonificación:", persona1.bonificacion())
persona1.tiempo_trabajo()
print()

persona2.mostrar_datos()
print("Sueldo con bonificación:", persona2.bonificacion())
persona2.tiempo_trabajo()
print()

persona3.mostrar_datos()
print("Sueldo con bonificación:", persona3.bonificacion())
persona3.tiempo_trabajo()

