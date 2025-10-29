"""
BLOQUE 2
Ejercicio_6

    Este módulo aplica un descuento del 10% a una lista de productos
    utilizando la función map() y una expresión lambda.
    Se demuestra el uso de programación funcional en Python.

Conceptos aplicados:
    - Programación funcional
    - map() y lambda
    - Trabajo con diccionarios y listas
"""

from typing import List, Dict


def aplicar_descuento(productos: List[Dict[str, float]]) -> List[Dict[str, float]]:
    """
    Aplica un descuento del 10% a una lista de productos.

    Args:
        productos (List[Dict[str, float]]):
            Lista de diccionarios que contienen el nombre y precio de cada producto.
            Ejemplo: [{"nombre": "Camisa", "precio": 50000}, ...]

    Returns:
        List[Dict[str, float]]:
            Nueva lista con cada producto, su precio original y su precio con descuento.
    """
    return list(map(lambda p: {
        "nombre": p["nombre"],
        "precio_original": p["precio"],
        "precio_descuento": p["precio"] * 0.9  # Aplica descuento del 10%
    }, productos))


if __name__ == "__main__":
    # Lista de productos de ejemplo
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000},
        {"nombre": "Gorra", "precio": 30000}
    ]

    # Aplicamos el descuento
    productos_descuento = aplicar_descuento(productos)

    # Mostramos resultados con formato bonito
    print("=== LISTA DE PRODUCTOS CON DESCUENTO ===")
    for p in productos_descuento:
        print(f"{p['nombre']}: Precio original ${p['precio_original']} → "
              f"Precio con descuento ${p['precio_descuento']:.2f}")
