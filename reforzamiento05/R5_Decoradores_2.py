# Reforzamiento 5

## Modulo

### Ejercicio 2
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


def decorador_multiplicacion(funcion):
    def datos_internos(*args, **kwargs):
        print("Está por ejecutarse la función")

        resultado = funcion(*args, **kwargs)

        print("La función ha sido ejecutado correctamente")
        return resultado

    return datos_internos

@decorador_multiplicacion
def multiplicar_valores(a, b, c, **kwargs):
    d = kwargs.get('d', 1)
    e = kwargs.get('e', 1)
    f = kwargs.get('f', 1)

    total = a * b * c * d * e * f
    print(f"Resultado de la multiplicación: {total}")
    return total

multiplicar_valores(2, 3, 4, d=1, e=2, f=5)
print()
multiplicar_valores(1, 1, 1, d=10, e=10, f=10)
print()
multiplicar_valores(5, 2, 1, d=2, e=3, f=4)

