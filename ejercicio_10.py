"""
BLOQUE 2
Ejercicio_10

    Este módulo implementa una función recursiva llamada explorar_estructura()
    que puede recorrer estructuras de datos anidadas como listas, diccionarios
    o combinaciones de ambos, imprimiendo los valores no iterables junto con
    su nivel de profundidad.

Conceptos aplicados:
    - Recursividad
    - Caso base
    - isinstance()
    - Type Hinting (Any)
"""

from typing import Any


def explorar_estructura(elemento: Any, profundidad: int = 1) -> None:
    """
    Explora recursivamente una estructura de datos (listas, diccionarios, tuplas, etc.)
    e imprime cada valor no iterable junto con su profundidad.

    Args:
        elemento (Any): Elemento o estructura de datos a explorar.
        profundidad (int): Nivel actual de profundidad (por defecto 1).

    Returns:
        None
    """
    # Caso base: si el elemento no es una lista, tupla ni diccionario
    if not isinstance(elemento, (list, tuple, dict)):
        print(f"Valor: {elemento}, Profundidad: {profundidad}")
        return

    # Si es una lista o tupla, recorrer cada elemento
    if isinstance(elemento, (list, tuple)):
        for sub_elemento in elemento:
            explorar_estructura(sub_elemento, profundidad + 1)

    # Si es un diccionario, recorrer sus valores
    elif isinstance(elemento, dict):
        for valor in elemento.values():
            explorar_estructura(valor, profundidad + 1)


if __name__ == "__main__":
    # Ejemplo de prueba directa
    estructura = [1, [2, 3], {"a": 4, "b": [5, {"c": 6}]}]
    print("Explorando estructura compleja:")
    explorar_estructura(estructura)
