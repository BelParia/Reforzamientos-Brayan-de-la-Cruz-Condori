# Reforzamiento 5

## Modulo

### Ejercicio 4
"""
Creando un archivo principal (main4.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones: - Una función que genere 30 números enteros aleatorios entre 0 y
100, y muestre en pantalla esta lista de números aleatorios - Otra función que ordene los valores de una lista y volver a mostrarla
en pantalla - Otra función que me indicará cuál es el mayor de todos estos
números de la lista
Uso de la función random:
"""

import math

def cargar_valor():
    while True:
        valor = input("Ingrese un número entero: ")
        if valor.isdigit():
            return int(valor)
        else:
            print("Error: Solo se permiten números enteros. Intente nuevamente.")

def mostrar_raiz_cuadrada(numero):
    raiz = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {raiz:.2f}")

def calcular_potencias(numero):
    resultados = {
        "cuadrado": math.pow(numero, 2),
        "cubo": math.pow(numero, 3)
    }
    return resultados

