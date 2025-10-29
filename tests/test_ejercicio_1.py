"""
Pruebas unitarias para el Ejercicio 1: Calculadora de IMC.

Estas pruebas validan que las funciones calcular_imc() e interpretar_imc()
funcionen correctamente para distintos escenarios, incluyendo casos borde.
"""

import pytest
from ejercicio_1 import calcular_imc, interpretar_imc


def test_calcular_imc_normal():
    """Prueba un caso normal de IMC."""
    resultado = calcular_imc(70, 1.75)
    assert round(resultado, 2) == 22.86  # IMC ≈ 22.86


def test_calcular_imc_borde():
    """Prueba con un valor borde (persona muy baja o muy liviana)."""
    resultado = calcular_imc(40, 1.50)
    assert round(resultado, 2) == 17.78  # IMC bajo peso


def test_interpretar_imc_bajo_peso():
    """Debe identificar correctamente el bajo peso."""
    assert interpretar_imc(17.5) == "Bajo peso"


def test_interpretar_imc_normal():
    """Debe identificar un IMC normal."""
    assert interpretar_imc(22.0) == "Normal"


def test_interpretar_imc_sobrepeso():
    """Debe identificar correctamente el sobrepeso."""
    assert interpretar_imc(27.0) == "Sobrepeso"


def test_interpretar_imc_obesidad():
    """Debe identificar correctamente la obesidad."""
    assert interpretar_imc(32.5) == "Obesidad"
