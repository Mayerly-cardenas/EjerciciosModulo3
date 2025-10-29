"""
BLOQUE 2
Ejercicio_7

    Este módulo filtra una lista de estudiantes utilizando la función filter()
    y una expresión lambda para obtener solo aquellos que aprobaron
    (nota mayor o igual a 3.0).

Conceptos aplicados:
    - filter() y lambda
    - Trabajo con tuplas
    - Programación funcional
"""

from typing import List, Tuple


def filtrar_aprobados(estudiantes: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
    """
    Filtra una lista de estudiantes, devolviendo solo los que tienen una nota >= 3.0.

    Args:
        estudiantes (List[Tuple[str, float]]):
            Lista de tuplas donde cada tupla contiene el nombre y la nota de un estudiante.
            Ejemplo: [("Ana", 4.5), ("Juan", 2.8), ("Maria", 3.9)]

    Returns:
        List[Tuple[str, float]]:
            Nueva lista con los estudiantes que aprobaron.
    """
    return list(filter(lambda e: e[1] >= 3.0, estudiantes))


if __name__ == "__main__":
    # Lista de estudiantes ejemplo
    estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("Maria", 3.9), ("Luis", 2.5), ("Camila", 3.2)]

    # Aplicamos el filtro para obtener los aprobados
    aprobados = filtrar_aprobados(estudiantes)

    # Mostramos los resultados
    print("=== ESTUDIANTES APROBADOS ===")
    for nombre, nota in aprobados:
        print(f"{nombre} - Nota: {nota}")
