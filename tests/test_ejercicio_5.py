import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ejercicio_5 import calcular_iva, actualizar_tasa_iva, TASA_IVA


def test_calcular_iva_por_defecto():
    precio = 100.0
    resultado = calcular_iva(precio)
    assert resultado == 19.0  # 19% de 100


def test_actualizar_tasa_iva_y_recalculo():
    # Guardar tasa original
    from ejercicio_5 import TASA_IVA
    tasa_original = TASA_IVA

    # Actualizar la tasa a 10%
    actualizar_tasa_iva(0.10)
    resultado = calcular_iva(200.0)
    assert resultado == 20.0  # 10% de 200

    # Restaurar la tasa original para no afectar otras pruebas
    actualizar_tasa_iva(tasa_original)


def test_actualizar_tasa_invalida():
    import pytest
    with pytest.raises(ValueError):
        actualizar_tasa_iva(1.5)  # Valor fuera del rango permitido


def test_actualizar_tasa_a_cero():
    actualizar_tasa_iva(0.0)
    assert calcular_iva(500.0) == 0.0
    # Restaurar tasa a 0.19
    actualizar_tasa_iva(0.19)
