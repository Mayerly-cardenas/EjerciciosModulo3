"""
Ejercicio 4: Validador de Datos Genérico

Este módulo implementa una función de orden superior que aplica un validador
a una lista de datos y devuelve solo los que pasan la validación.
"""

from typing import List, Callable


def aplicar_validador(datos: List, validador: Callable) -> List:
    """
    Aplica una función de validación a cada elemento de la lista y devuelve
    los elementos que pasan la validación.

    Args:
        datos (List): Lista de datos a validar.
        validador (Callable): Función que recibe un elemento y devuelve True/False.

    Returns:
        List: Nueva lista con los elementos válidos.
    """
    return [d for d in datos if validador(d)]


def es_email_valido(email: str) -> bool:
    """
    Valida si un string tiene formato básico de email.
    """
    return "@" in email and "." in email and not email.startswith("@") and not email.endswith(".")


def es_mayor_a_10(numero: int) -> bool:
    """
    Valida si un número entero es mayor a 10.
    """
    return numero > 10
