# Reforzamiento 5

## Modulo

### Ejercicio 3
"""
Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones: - Una función que genere 30 números enteros aleatorios entre 0 y
100, y muestre en pantalla esta lista de números aleatorios - Otra función que ordene los valores de una lista y volver a mostrarla
en pantalla - Otra función que me indicará cuál es el mayor de todos estos
números de la lista
Uso de la función random:
"""

# para generar números aleatorios
from random import randint

def generar_lista():
    lista = [randint(0, 100) for _ in range(30)]
    print("Lista generada:")
    print(lista)
    return lista


def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("\nLista ordenada:")
    print(lista_ordenada)
    return lista_ordenada


def numero_mayor(lista):
    mayor = max(lista)
    print(f"\nEl número mayor de la lista es {mayor}")
    return mayor

