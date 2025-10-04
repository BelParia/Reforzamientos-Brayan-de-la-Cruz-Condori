# Reforzamiento 5

## Clases

### Ejercicio 1
"""
Crear una clase Empleado que contenga los siguientes métodos, uno que
pida ingresar un nombre, apellido y edad, un método para pedir su sueldo
actual y otro métod0 que lo imprima ambos resultados, pero estarán
contenidos en un diccionario. Comprobar los métodos instanciado la clase
respectivamente al menos para 3 empleados. Considerar en el constructor los
valores necesarios.
"""

class Empleado:
    def __init__(self, nombre="", apellido="", edad=0, sueldo=0):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sueldo = sueldo

    def ingresar_datos(self):
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")
        self.edad = int(input("Ingrese la edad (en años): "))

    def ingresar_sueldo(self):
        self.sueldo = float(input("Ingrese el sueldo actual del empleado: "))

    def mostrar_datos(self):
        datos = {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Edad": self.edad,
            "Sueldo": self.sueldo
        }
        print(datos)

"""Las 3 instancias se muestran a continuación"""
empleado1 = Empleado()
empleado1.ingresar_datos()
empleado1.ingresar_sueldo()
empleado1.mostrar_datos()

empleado2 = Empleado()
empleado2.ingresar_datos()
empleado2.ingresar_sueldo()
empleado2.mostrar_datos()

empleado3 = Empleado()
empleado3.ingresar_datos()
empleado3.ingresar_sueldo()
empleado3.mostrar_datos()

