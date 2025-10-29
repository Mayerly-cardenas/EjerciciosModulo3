"""
BLOQUE 2
Ejercicio_8

    Este módulo procesa un texto y aplica transformaciones utilizando
    List Comprehension y Dictionary Comprehension.
    Primero obtiene las palabras con más de 5 letras en mayúsculas,
    y luego crea un diccionario que relaciona cada palabra con su longitud.

Conceptos aplicados:
    - List Comprehensions
    - Dictionary Comprehensions
    - Métodos de cadena (split, upper)
"""

from typing import List, Dict, Tuple


def transformar_texto(texto: str) -> Tuple[List[str], Dict[str, int]]:
    """
    Transforma un texto en una lista de palabras con más de 5 letras en mayúsculas
    y un diccionario con las longitudes de cada palabra.

    Args:
        texto (str): Texto de entrada.

    Returns:
        Tuple[List[str], Dict[str, int]]:
            - Lista de palabras en mayúsculas con más de 5 letras.
            - Diccionario que relaciona cada palabra con su longitud.
    """
    # Dividir el texto en palabras y filtrar las de más de 5 letras, convirtiéndolas en mayúsculas
    palabras_filtradas = [palabra.upper() for palabra in texto.split() if len(palabra) > 5]

    # Crear un diccionario con la palabra y su longitud
    longitudes = {palabra: len(palabra) for palabra in palabras_filtradas}

    return palabras_filtradas, longitudes


if __name__ == "__main__":
    texto_ejemplo = (
        "La programación en Python es extremadamente poderosa y divertida "
        "cuando se aprende a utilizar correctamente las comprensiones."
    )

    palabras, diccionario = transformar_texto(texto_ejemplo)

    print("=== PALABRAS FILTRADAS (más de 5 letras, en mayúsculas) ===")
    print(palabras)

    print("\n=== DICCIONARIO DE LONGITUDES ===")
    print(diccionario)
