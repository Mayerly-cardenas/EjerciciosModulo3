"""
BLOQUE 1
Ejercicio 5: Calculadora de Impuestos con Scope Global

Este módulo simula el cálculo de impuestos (IVA) donde la tasa puede cambiar.
Se muestra cómo usar y modificar variables globales correctamente.
"""

# Variable global
TASA_IVA = 0.19


def calcular_iva(precio_base: float) -> float:
    """
    Calcula el valor del IVA con base en la tasa global TASA_IVA.

    Args:
        precio_base (float): Precio del producto antes de impuestos.

    Returns:
        float: Valor del IVA calculado.
    """
    return round(precio_base * TASA_IVA, 2)


def actualizar_tasa_iva(nueva_tasa: float) -> None:
    """
    Actualiza el valor global de la tasa de IVA.

    Args:
        nueva_tasa (float): Nuevo valor decimal de la tasa (por ejemplo, 0.16 para 16%).

    Returns:
        None
    """
    global TASA_IVA
    if not (0 <= nueva_tasa <= 1):
        raise ValueError("La tasa de IVA debe estar entre 0 y 1.")
    TASA_IVA = nueva_tasa
