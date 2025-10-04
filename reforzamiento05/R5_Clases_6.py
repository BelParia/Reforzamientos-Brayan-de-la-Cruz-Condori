# Reforzamiento 5

## Clases

### Ejercicio 6, en el documento no sigue el orden adecuado
"""
Desarrolla una clase Agenda que administrará contactos. Dentro de una
lista se debe almacenar un diccionario para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto, Mostrar contactos y Buscar contacto (Por DNI)
Estructura de la lista cada vez que vas agregando un contacto:
contactos = [
{‘nombre’: “Luis”, ‘telefono’: “997667945”, ‘email’: “luishh@gmail.com”, ‘dni’:
44234239},
{‘nombre’: “Milagros”, ‘telefono’: “997654687”, ‘email’:
“milagros19c@gmail.com”, ‘dni’: 43423211}
]
Agregar por lo menos 4 personas (instanciándolas) para poder luego realizar
la búsqueda de estas personas en la agenda y saber si existen, en caso
contrario indicar: “´Nombre´ no se encuentra anotado en la agenda”
"""

class Agenda:
    def __init__(self):
        self.contactos = []

    def anadir_contacto(self, nombre, telefono, email, dni):
        contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email,
            "dni": dni
        }
        self.contactos.append(contacto)
        print(f"Contacto {nombre} añadido correctamente")

    def mostrar_contactos(self):
        print("\nLista de contactos:")
        for contac in self.contactos:
            print(f"Nombre: {contac['nombre']}, Teléfono: {contac['telefono']}, Email: {contac['email']}, DNI: {contac['dni']}")
        print()

    def buscar_contacto(self, dni):  # como de indica: es una busqueda por DNI, talvez la función debería llamarse buscar_contacto_dni
        for contac in self.contactos:
            if contac['dni'] == dni:
                print(f"Contacto encontrado: {contac['nombre']} \n- Tel: {contac['telefono']} \n- Email: {contac['email']}\n")
                return
        print(f"No se encuentra ningún contacto con DNI {dni} en la agenda.\n"
              f"Verifica los digitos del DNI, en todo caso añade denuevo el contacto.")

mi_agenda = Agenda()

mi_agenda.anadir_contacto("Roly", "918840047", "roly.condori@unmsm.edu.com", 75529670)
mi_agenda.anadir_contacto("Milagritos", "997654687", "milagritos19c@gmail.com", 43423211)
mi_agenda.anadir_contacto("Pepe", "988776655", "big_pepe22@gmail.com", 44567890)
mi_agenda.anadir_contacto("Carmesí", "912345678", "carmesi.castañeda@gmail.com", 43789456)

mi_agenda.mostrar_contactos()

# Busqueda de contacntos con solo DNI
mi_agenda.buscar_contacto(44567890)
mi_agenda.buscar_contacto(11111111)

