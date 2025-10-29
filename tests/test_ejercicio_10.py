"""
Módulo de pruebas unitarias para ejercicio_10.py
Verifica el correcto funcionamiento de la función recursiva explorar_estructura().
"""

import io
import sys
from ejercicio_10 import explorar_estructura


def capturar_salida(funcion, *args, **kwargs):
    """
    Captura la salida impresa de una función (print) y la devuelve como texto.
    """
    salida = io.StringIO()
    sys.stdout = salida
    funcion(*args, **kwargs)
    sys.stdout = sys.__stdout__
    return salida.getvalue()


def test_explorar_estructura_lista_simple():
    """
    Verifica que se impriman correctamente los valores y profundidades
    en una lista simple.
    """
    estructura = [1, 2, 3]
    salida = capturar_salida(explorar_estructura, estructura)
    assert "Valor: 1, Profundidad: 2" in salida
    assert "Valor: 3, Profundidad: 2" in salida


def test_explorar_estructura_anidada():
    """
    Verifica el recorrido correcto de estructuras anidadas combinadas.
    """
    estructura = [1, [2, 3], {"a": 4, "b": [5, {"c": 6}]}]
    salida = capturar_salida(explorar_estructura, estructura)

    # Verificamos que ciertos valores clave estén en la salida
    assert "Valor: 1, Profundidad: 2" in salida
    assert "Valor: 2, Profundidad: 3" in salida
    assert "Valor: 4, Profundidad: 3" in salida
    assert "Valor: 6, Profundidad: 5" in salida
