import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ejercicio_2 import crear_perfil


def test_crear_perfil_completo():
    resultado = crear_perfil(
        "Mayerly",
        22,
        "Leer", "Programar", "Escuchar música",
        twitter="@mayerlyC",
        instagram="@mayerly_22"
    )
    assert "Mayerly" in resultado
    assert "Leer" in resultado
    assert "Programar" in resultado
    assert "Twitter: @mayerlyC" in resultado
    assert "Instagram: @mayerly_22" in resultado


def test_crear_perfil_sin_hobbies():
    resultado = crear_perfil("Juan", 25, twitter="@juan25")
    assert "Hobbies: Ninguno registrado" in resultado
    assert "Twitter: @juan25" in resultado


def test_crear_perfil_sin_redes():
    resultado = crear_perfil("Tatiana", 20, "Cantar", "Bailar")
    assert "Cantar" in resultado
    assert "Bailar" in resultado
    assert "Redes Sociales: Ninguna registrada" in resultado


def test_crear_perfil_vacio():
    resultado = crear_perfil("Anonimo", 0)
    assert "Anonimo" in resultado
    assert "0 años" in resultado
    assert "Hobbies: Ninguno registrado" in resultado
    assert "Redes Sociales: Ninguna registrada" in resultado
