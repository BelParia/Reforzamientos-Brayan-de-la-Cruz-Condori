# Reforzamiento 5

## Modulo

### Ejercicio 4
"""
Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones: - Una función que genere 30 números enteros aleatorios entre 0 y
100, y muestre en pantalla esta lista de números aleatorios - Otra función que ordene los valores de una lista y volver a mostrarla
en pantalla - Otra función que me indicará cuál es el mayor de todos estos
números de la lista
Uso de la función random:
"""

#importamos nuestro módulo en donde estan las operaciones o funciones de la misma
import main4

valores_correctos = main4.cargar_valor()
raiz = main4.mostrar_raiz_cuadrada(valores_correctos)
potencias = main4.calcular_potencias(valores_correctos)
print(f"El número {valores_correctos} elevado al cuadrado es: {potencias['cuadrado']}")
print(f"El número {valores_correctos} elevado al cubo es: {potencias['cubo']}")


