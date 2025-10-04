# Reforzamiento 5

## Modulo

### Ejercicio 1
"""
Crear una función decoradora que dará los buenos días antes de
ejecutar una función llamada saludo_inicial(nombre) a ser decorada
“Buenos días NOMBRE son las HORA horas con MINUTOS minutos” y
luego de ser ejecutada lanzará un mensaje diciendo “Hasta luego
NOMBRE que tenga buen día”.
La función a decorar pedirá el nombre de una persona y retornará el
mensaje.
Usar la función decorada al menos 3 veces 
"""

from datetime import datetime

def buenos_dias_decorador(funcion):
    def datos_internos(nombre):
        ahora = datetime.now()
        hora = ahora.hour
        minu = ahora.minute
        print(f"Buenos días, {nombre}, son las {hora} horas con {minu} minutos")

        resultado = funcion(nombre)

        print(f"Hasta luego, {nombre}, que tenga buen día")
        return resultado

    return datos_internos

@buenos_dias_decorador
def saludo_inicial(nombre):
    return f"Hola {nombre}, bienvenido al curso."

print(saludo_inicial("Brayan"))
print()
print(saludo_inicial("Mirían"))
print()
print(saludo_inicial("Roly"))
