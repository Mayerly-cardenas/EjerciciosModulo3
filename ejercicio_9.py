"""
BLOQUE 2
Ejercicio_9

    Este módulo utiliza functools.reduce y funciones lambda para:
        1. Calcular la suma total de una lista de números.
        2. Concatenar una lista de strings en una sola frase.

Conceptos aplicados:
    - functools.reduce
    - Funciones lambda
    - Programación funcional
"""

from typing import List
from functools import reduce


def sumar_lista(numeros: List[int]) -> int:
    """
    Calcula la suma total de una lista de números utilizando reduce y lambda.

    Args:
        numeros (List[int]): Lista de números enteros.

    Returns:
        int: Suma total de los números.
    """
    return reduce(lambda x, y: x + y, numeros)


def concatenar_strings(cadenas: List[str]) -> str:
    """
    Concatena una lista de strings en una sola cadena utilizando reduce y lambda.

    Args:
        cadenas (List[str]): Lista de strings.

    Returns:
        str: Cadena concatenada resultante.
    """
    return reduce(lambda x, y: x + y, cadenas)


if __name__ == "__main__":
    # Ejemplo de lista numérica
    numeros = [1, 2, 3, 4, 5]
    suma_total = sumar_lista(numeros)
    print(f"Suma total de {numeros}: {suma_total}")

    # Ejemplo de lista de cadenas
    palabras = ["Hola", " ", "SENA", "!"]
    frase = concatenar_strings(palabras)
    print(f"Frase concatenada: {frase}")
