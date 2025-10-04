# Reforzamiento 5

## Modulo

### Ejercicio 1, AQUÍ SE ENCUENTRA LA FUNCIÓN NECESARIA
"""
Crear un módulo que validará nombres de usuarios. Dicho módulo,
deberá tener una función y cumplir con los siguientes requisitos:
- Crear un archivo principal (main.py) donde importará al módulo
creado.
- El nombre de usuario debe tener una longitud mínima de 7
caracteres y un máximo de 12.
- El nombre de usuario debe ser alfanumérico (usar isalnum())
- Nombre de usuario con menos de 7 caracteres, retorna el mensaje
"El nombre de usuario debe contener al menos 7 caracteres".
- Nombre de usuario con más de 12 caracteres, retorna el mensaje
"El nombre de usuario no puede contener más de 12 caracteres".
- Nombre de usuario con caracteres distintos a los alfanuméricos,
retorna el mensaje "El nombre de usuario puede contener solo
letras y números".
- Si el nombre de usuario es válido, la función retornará True.
"""

def validar_usuario(nombre_usuario):
    # longitud mínima
    if len(nombre_usuario) <= 7:
        return "El nombre de usuario debe contener al menos 7 caracteres"

    # longitud máxima
    elif len(nombre_usuario) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres"

    # Verificar que sea alfanumérico
    elif not nombre_usuario.isalnum():
        return "El nombre de usuario puede contener solo letras y números"

    else:
        return True

