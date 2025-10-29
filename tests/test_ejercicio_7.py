"""
Módulo de pruebas unitarias para ejercicio_7.py
Verifica que la función filtrar_aprobados() filtre correctamente
a los estudiantes con nota >= 3.0 usando pytest.
"""

from ejercicio_7 import filtrar_aprobados


def test_filtrar_aprobados():
    """
    Comprueba que solo los estudiantes con nota >= 3.0 sean devueltos.
    """
    estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("Maria", 3.9), ("Pedro", 1.9), ("Laura", 3.0)]

    # Ejecutamos la función
    resultado = filtrar_aprobados(estudiantes)

    # Resultado esperado
    esperado = [("Ana", 4.5), ("Maria", 3.9), ("Laura", 3.0)]

    assert resultado == esperado, f"Error: esperado {esperado}, pero se obtuvo {resultado}"
