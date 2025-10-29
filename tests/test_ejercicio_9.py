"""
Módulo de pruebas unitarias para ejercicio_9.py
Verifica que las funciones sumar_lista() y concatenar_strings()
funcionen correctamente.
"""

from ejercicio_9 import sumar_lista, concatenar_strings


def test_sumar_lista():
    """
    Comprueba que la función sumar_lista() calcule correctamente la suma total.
    """
    numeros = [1, 2, 3, 4, 5]
    resultado = sumar_lista(numeros)
    esperado = 15
    assert resultado == esperado, f"Error: se esperaba {esperado}, pero se obtuvo {resultado}"


def test_concatenar_strings():
    """
    Comprueba que concatenar_strings() una correctamente todas las cadenas.
    """
    cadenas = ["Hola", " ", "SENA", "!"]
    resultado = concatenar_strings(cadenas)
    esperado = "Hola SENA!"
    assert resultado == esperado, f"Error: se esperaba '{esperado}', pero se obtuvo '{resultado}'"
