# Reforzamiento 5

## Modulo

### Ejercicio 2, AQUÍ SE ENCUENTRA LA FUNCIÓN NECESARIA
"""
Creando un archivo principal (main.py) donde llamará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones: - La primera función cargará a 3 números enteros que pedirá al
usuario que ingrese por consola un valor. - La segunda función solamente obtendrá la media de estos valores. - La última función te indicará cuál es el mayor de los 3 números - Desde el archivo principal importar al módulo y las funciones
correspondiente usando las funciones anteriormente creadas en el
módulo. - Usarlo al menos para 3 casos distintos.
"""

# operaciones.py

def cargar_numeros():
    print("Ingrese tres números enteros:")
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    numero3 = int(input("Número 3: "))
    return numero1, numero2, numero3

def calcular_media(numero1, numero2, numero3):
    media = (numero1 + numero2 + numero3) / 3
    return media

def numero_mayor(numero1, numero2, numero3):
    mayor = max(numero1, numero2, numero3)
    return mayor

