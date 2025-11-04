import os
import csv
import pytest
from ejercicio_12 import analizar_csv


@pytest.fixture
def archivo_csv_temporal(tmp_path):
    """
    Crea un archivo CSV temporal con datos de prueba para el test.
    Retorna la ruta del archivo creado.
    """
    ruta = tmp_path / "estudiantes.csv"
    with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "edad", "calificación"])
        escritor.writerow(["Mayerly", "22", "4.5"])
        escritor.writerow(["Juan", "25", "3.8"])
        escritor.writerow(["Tatiana", "23", "4.9"])
        escritor.writerow(["Olga", "30", "4.1"])
    return ruta


def test_analizar_csv_correcto(archivo_csv_temporal):
    """
    Prueba que la función analizar_csv calcule correctamente el promedio, máximo y mínimo.
    """
    resultado = analizar_csv(str(archivo_csv_temporal), "calificación")

    assert isinstance(resultado, dict)
    assert pytest.approx(resultado["promedio"], 0.01) == 4.33  # Promedio esperado
    assert resultado["máximo"] == 4.9
    assert resultado["mínimo"] == 3.8


def test_analizar_csv_columna_inexistente(archivo_csv_temporal, capsys):
    """
     Prueba que la función maneje correctamente el caso de una columna inexistente.
    """
    resultado = analizar_csv(str(archivo_csv_temporal), "nota_invalida")

    captured = capsys.readouterr()
    assert "No se encontraron valores numéricos válidos" in captured.out
    assert resultado == {}


def test_analizar_csv_archivo_inexistente(capsys):
    """
     Prueba que la función maneje correctamente cuando el archivo no existe.
    """
    resultado = analizar_csv("archivo_que_no_existe.csv", "calificación")

    captured = capsys.readouterr()
    assert "no existe" in captured.out.lower()
    assert resultado == {}
