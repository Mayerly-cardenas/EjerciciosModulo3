"""
Módulo de pruebas unitarias para ejercicio_6.py
Usa pytest para verificar que la función aplicar_descuento()
calcula correctamente el precio con un 10% de descuento.
"""

from ejercicio_6 import aplicar_descuento


def test_aplicar_descuento():
    """
    Verifica que los precios con descuento sean correctos.
    """
    # Datos de entrada
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000},
        {"nombre": "Gorra", "precio": 30000}
    ]

    # Resultado esperado (10% de descuento aplicado)
    precios_esperados = [45000.0, 72000.0, 108000.0, 27000.0]

    # Ejecutamos la función
    productos_descuento = aplicar_descuento(productos)
    precios_obtenidos = [p["precio_descuento"] for p in productos_descuento]

    # Comprobamos igualdad exacta
    assert precios_obtenidos == precios_esperados, (
        f"Error: se esperaba {precios_esperados}, pero se obtuvo {precios_obtenidos}"
    )
