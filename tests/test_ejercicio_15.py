import json
import pytest
from ejercicio_15 import (
    cargar_biblioteca,
    guardar_biblioteca,
    prestar_libro,
    devolver_libro,
    buscar_libro,
    ver_libros_prestados,
)

@pytest.fixture
def biblioteca_temp(tmp_path):
    archivo = tmp_path / "biblioteca.json"
    datos = [
        {"libro_id": "001", "titulo": "Cien Años de Soledad", "prestado_a": None},
        {"libro_id": "002", "titulo": "El Principito", "prestado_a": "Tatiana"},
    ]
    archivo.write_text(json.dumps(datos), encoding="utf-8")
    return archivo, datos

def test_cargar_y_guardar_biblioteca(biblioteca_temp):
    archivo, datos = biblioteca_temp
    cargado = cargar_biblioteca(archivo)
    assert len(cargado) == 2
    guardar_biblioteca(archivo, cargado)
    nuevo = json.loads(archivo.read_text(encoding="utf-8"))
    assert nuevo == cargado

def test_prestar_libro(biblioteca_temp):
    _, datos = biblioteca_temp
    msg = prestar_libro("001", "Mayerly", datos)
    assert "prestado a Mayerly" in msg
    assert datos[0]["prestado_a"] == "Mayerly"

def test_devolver_libro(biblioteca_temp):
    _, datos = biblioteca_temp
    msg = devolver_libro("002", datos)
    assert "devuelto correctamente" in msg
    assert datos[1]["prestado_a"] is None

def test_buscar_libro(biblioteca_temp):
    _, datos = biblioteca_temp
    resultado = buscar_libro("Soledad", datos)
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "Cien Años de Soledad"

def test_ver_libros_prestados(biblioteca_temp):
    _, datos = biblioteca_temp
    prestados = ver_libros_prestados(datos)
    assert len(prestados) == 1
    assert prestados[0]["prestado_a"] == "Tatiana"
