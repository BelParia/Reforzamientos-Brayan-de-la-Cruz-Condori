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

#importamos nuestro módulo en donde estan las operaciones o funciones de la misma
import main3

numeros = main3.generar_lista()

numeros_ordenados = main3.ordenar_lista(numeros)

main3.numero_mayor(numeros_ordenados)

