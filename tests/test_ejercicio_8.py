"""
Módulo de pruebas unitarias para ejercicio_8.py
Verifica que la función transformar_texto() funcione correctamente.
"""

from ejercicio_8 import transformar_texto


def test_transformar_texto():
    """
    Comprueba que las palabras con más de 5 letras se filtren correctamente
    y que el diccionario de longitudes sea el esperado.
    """
    texto = "Python es un lenguaje poderoso y educativo"
    palabras, longitudes = transformar_texto(texto)

    # Palabras esperadas con más de 5 letras, en mayúsculas
    esperado_palabras = ["PYTHON", "LENGUAJE", "PODEROSO", "EDUCATIVO"]

    # Diccionario esperado
    esperado_longitudes = {
        "PYTHON": 6,
        "LENGUAJE": 8,
        "PODEROSO": 8,
        "EDUCATIVO": 9
    }

    assert palabras == esperado_palabras, f"Error: se esperaba {esperado_palabras}, pero se obtuvo {palabras}"
    assert longitudes == esperado_longitudes, f"Error: se esperaba {esperado_longitudes}, pero se obtuvo {longitudes}"
