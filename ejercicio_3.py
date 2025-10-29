"""
BLOQUE 1
Ejercicio 3: Contador de Llamadas con Closure

Este módulo implementa una fábrica de contadores usando funciones anidadas
y el concepto de closures.
"""


def crear_contador():
    """
    Crea un contador independiente que aumenta cada vez que se llama
    la función retornada.

    Retorna:
        function: Una función interna que incrementa y devuelve el conteo.
    """
    conteo = 0

    def incrementar():
        nonlocal conteo
        conteo += 1
        return conteo

    return incrementar
