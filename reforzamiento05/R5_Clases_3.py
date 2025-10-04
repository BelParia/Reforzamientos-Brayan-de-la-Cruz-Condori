# Reforzamiento 5

## Clases

### Ejercicio 3 o 4, en el documento no sigue el orden adecuado
"""
Crear una clase Alumno que tenga como atributos el nombre, edad y la
nota final del alumno. Crear los métodos para inicializar sus atributos, otro
para imprimirlos y un métod0 para mostrar un mensaje con el resultado de la
nota, si ha aprobado (mayor o igual a 13) o no el alumno. Instanciar la clase
por lo menos 4 veces (4 alumnos)
"""

class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Nota Final: {self.nota_final}")

    def resultado(self):
        if self.nota_final >= 13:
            print(f"{self.nombre}, la fe, la fe: alumno, ha aprobado")
        else:
            print(f"{self.nombre}, lamentablemente, ha desaprobado")

alumno1 = Alumno("María", 18, 15)
alumno2 = Alumno("Brayan", 19, 11)
alumno3 = Alumno("Roberta", 17, 13)
alumno4 = Alumno("Roly", 20, 10)

alumno1.mostrar_datos()
alumno1.resultado()

alumno2.mostrar_datos()
alumno2.resultado()

alumno3.mostrar_datos()
alumno3.resultado()

alumno4.mostrar_datos()
alumno4.resultado()

