"""
Pruebas unitarias para el Ejercicio 11: Gestor de Tareas en Archivo de Texto (.txt)

Este conjunto de pruebas valida que las funciones principales del gestor
funcionen correctamente:
- Crear el archivo automáticamente al agregar una tarea.
- Agregar nuevas tareas al archivo.
- Leer correctamente las tareas existentes.
"""

import sys
import os
import io
from pathlib import Path

# Asegurar acceso al archivo principal
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ejercicio_11 import agregar_tarea, ver_tareas


def test_agregar_tarea_crea_archivo(tmp_path, monkeypatch):
    """
    Verifica que al agregar una tarea:
    - Se cree el archivo si no existe.
    - La tarea se guarde correctamente en el archivo.
    """
    # Ruta temporal para evitar modificar tareas reales
    archivo_temporal = tmp_path / "tareas_test.txt"

    # Simular variable global ARCHIVO_TAREAS apuntando al archivo temporal
    import ejercicio_11
    monkeypatch.setattr(ejercicio_11, "ARCHIVO_TAREAS", str(archivo_temporal))

    # Ejecutar función
    agregar_tarea("Tarea de prueba")

    # Validar que el archivo se creó
    assert archivo_temporal.exists(), "El archivo no fue creado automáticamente."

    # Leer contenido
    contenido = archivo_temporal.read_text(encoding="utf-8").strip()
    assert "Tarea de prueba" in contenido, "La tarea no se guardó correctamente."


def test_ver_tareas_devuelve_lista(tmp_path, monkeypatch):
    """
    Verifica que ver_tareas() devuelva una lista con las tareas del archivo.
    """
    archivo_temporal = tmp_path / "tareas_test.txt"
    archivo_temporal.write_text("Tarea A\nTarea B\n", encoding="utf-8")

    import ejercicio_11
    monkeypatch.setattr(ejercicio_11, "ARCHIVO_TAREAS", str(archivo_temporal))

    tareas = ver_tareas()

    assert isinstance(tareas, list), "ver_tareas() no devolvió una lista."
    assert len(tareas) == 2, "No se leyeron todas las tareas del archivo."
    assert "Tarea A" in tareas and "Tarea B" in tareas, "Las tareas no coinciden con el contenido."


def test_ver_tareas_archivo_inexistente(tmp_path, monkeypatch):
    """
    Verifica que ver_tareas() maneje correctamente cuando el archivo no existe.
    Debe devolver una lista vacía.
    """
    archivo_temporal = tmp_path / "no_existe.txt"

    import ejercicio_11
    monkeypatch.setattr(ejercicio_11, "ARCHIVO_TAREAS", str(archivo_temporal))

    tareas = ver_tareas()
    assert tareas == [], "Debe devolver una lista vacía si el archivo no existe."
