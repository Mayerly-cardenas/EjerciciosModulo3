import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ejercicio_3 import crear_contador


def test_contador_incrementa_correctamente():
    contador = crear_contador()
    assert contador() == 1
    assert contador() == 2
    assert contador() == 3


def test_contadores_independientes():
    contador_a = crear_contador()
    contador_b = crear_contador()

    assert contador_a() == 1
    assert contador_a() == 2

    assert contador_b() == 1  # independiente de contador_a
    assert contador_b() == 2

    # el contador_a sigue donde iba
    assert contador_a() == 3


def test_no_reinicia_cada_llamada():
    contador = crear_contador()
    valores = [contador() for _ in range(5)]
    assert valores == [1, 2, 3, 4, 5]
