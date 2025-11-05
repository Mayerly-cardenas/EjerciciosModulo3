import os
import json
import pytest
from io import StringIO
from rich.console import Console
from ejercicio_13 import (
    cargar_inventario,
    guardar_inventario,
    agregar_producto,
    vender_producto,
    mostrar_inventario
)

# Archivo temporal para pruebas
ARCHIVO_PRUEBA = "inventario_test.json"


@pytest.fixture
def limpiar_archivo():
    """Elimina el archivo de prueba antes y después de cada test."""
    if os.path.exists(ARCHIVO_PRUEBA):
        os.remove(ARCHIVO_PRUEBA)
    yield
    if os.path.exists(ARCHIVO_PRUEBA):
        os.remove(ARCHIVO_PRUEBA)


def test_cargar_inventario_vacio(limpiar_archivo):
    """Debe devolver lista vacía si el archivo no existe."""
    inventario = cargar_inventario(ARCHIVO_PRUEBA)
    assert inventario == []


def test_guardar_y_cargar_inventario(limpiar_archivo):
    """Debe guardar y cargar correctamente los datos."""
    datos = [{"nombre": "Manzanas", "cantidad": 10, "precio": 1.5}]
    guardar_inventario(datos, ARCHIVO_PRUEBA)

    cargado = cargar_inventario(ARCHIVO_PRUEBA)
    assert cargado == datos


def test_agregar_producto_nuevo(limpiar_archivo):
    """Debe agregar un nuevo producto al inventario."""
    inventario = []
    agregar_producto(inventario, "Pan", 5, 0.8)
    assert inventario == [{"nombre": "Pan", "cantidad": 5, "precio": 0.8}]


def test_agregar_producto_existente_suma_cantidad(limpiar_archivo):
    """Debe sumar cantidad si el producto ya existe."""
    inventario = [{"nombre": "Pan", "cantidad": 5, "precio": 0.8}]
    agregar_producto(inventario, "Pan", 3, 0.8)
    assert inventario[0]["cantidad"] == 8


def test_vender_producto_resta_cantidad(limpiar_archivo):
    """Debe restar la cantidad correctamente al vender."""
    inventario = [{"nombre": "Leche", "cantidad": 10, "precio": 2.0}]
    vender_producto(inventario, "Leche", 4)
    assert inventario[0]["cantidad"] == 6


def test_vender_producto_no_existente(capsys, limpiar_archivo):
    """Debe mostrar mensaje si el producto no existe."""
    inventario = [{"nombre": "Pan", "cantidad": 3, "precio": 0.8}]
    vender_producto(inventario, "Huevos", 2)
    captured = capsys.readouterr()
    assert "no encontrado" in captured.out.lower()


def test_mostrar_inventario_rich(capsys, limpiar_archivo):
    """Debe mostrar correctamente una tabla con rich."""
    inventario = [
        {"nombre": "Pan", "cantidad": 5, "precio": 0.8},
        {"nombre": "Leche", "cantidad": 2, "precio": 2.0},
    ]
    mostrar_inventario(inventario)
    captured = capsys.readouterr()
    assert "Pan" in captured.out
    assert "Leche" in captured.out
