# Reforzamiento 5

## Modulo

### Ejercicio 2, en el documento no sigue el orden adecuado
"""
Creando un archivo principal (main.py) donde llamará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones: - La primera función cargará a 3 números enteros que pedirá al
usuario que ingrese por consola un valor. - La segunda función solamente obtendrá la media de estos valores. - La última función te indicará cuál es el mayor de los 3 números - Desde el archivo principal importar al módulo y las funciones
correspondiente usando las funciones anteriormente creadas en el
módulo. - Usarlo al menos para 3 casos distintos.
"""

#importamos nuestro módulo en donde estan las operaciones o funciones de la misma
import main2

# caso 1
num1, num2, num3 = main2.cargar_numeros()
print("Media:", main2.calcular_media(num1, num2, num3))
print("Mayor:", main2.numero_mayor(num1, num2, num3))

# caso 2
num1, num2, num3 = main2.cargar_numeros()
print("Media:", main2.calcular_media(num1, num2, num3))
print("Mayor:", main2.numero_mayor(num1, num2, num3))

# caso 3
num1, num2, num3 = main2.cargar_numeros()
print("Media:", main2.calcular_media(num1, num2, num3))
print("Mayor:", main2.numero_mayor(num1, num2, num3))

