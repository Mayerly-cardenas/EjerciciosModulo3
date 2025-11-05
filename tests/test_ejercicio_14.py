import os
import json
import csv
import pytest
from ejercicio_14 import leer_csv, leer_json, generar_reporte

@pytest.fixture
def archivos_de_prueba(tmp_path):
    # Crear archivos temporales
    estudiantes = tmp_path / "estudiantes.csv"
    cursos = tmp_path / "cursos.json"
    reporte = tmp_path / "reporte.txt"

    # Datos de ejemplo
    estudiantes.write_text("id_estudiante,nombre\n1,Mayerly\n2,Tatiana\n", encoding="utf-8")
    cursos.write_text(json.dumps({"1": ["Python"], "2": ["HTML", "CSS"]}), encoding="utf-8")

    return estudiantes, cursos, reporte

def test_leer_csv(archivos_de_prueba):
    estudiantes, _, _ = archivos_de_prueba
    data = leer_csv(estudiantes)
    assert isinstance(data, list)
    assert data[0]["nombre"] == "Mayerly"

def test_leer_json(archivos_de_prueba):
    _, cursos, _ = archivos_de_prueba
    data = leer_json(cursos)
    assert "1" in data
    assert data["1"] == ["Python"]

def test_generar_reporte(archivos_de_prueba):
    estudiantes, cursos, reporte = archivos_de_prueba
    data_est = leer_csv(estudiantes)
    data_cursos = leer_json(cursos)
    generar_reporte(data_est, data_cursos, reporte)
    assert os.path.exists(reporte)
    contenido = reporte.read_text(encoding="utf-8")
    assert "Mayerly" in contenido
    assert "Python" in contenido
