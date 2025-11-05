"""
Ejercicio 13: Gestor de Inventario Persistente con JSON
Autor: Nubia Mayerly Cárdenas Bautista
Conceptos aplicados: json (load, dump), persistencia de datos, modularización,
listas y diccionarios, uso de la librería rich para mostrar tablas.
"""

import json
import os
from rich.console import Console
from rich.table import Table

# ============================
# FUNCIONES DEL INVENTARIO
# ============================

def cargar_inventario(nombre_archivo: str = "inventario.json") -> list:
    """Carga el inventario desde un archivo JSON."""
    if not os.path.exists(nombre_archivo):
        return []
    with open(nombre_archivo, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def guardar_inventario(inventario: list, nombre_archivo: str = "inventario.json") -> None:
    """Guarda el inventario actual en el archivo JSON."""
    with open(nombre_archivo, "w", encoding="utf-8") as file:
        json.dump(inventario, file, indent=4, ensure_ascii=False)


def agregar_producto(inventario: list, nombre: str, cantidad: int, precio: float) -> None:
    """Agrega un nuevo producto o actualiza la cantidad si ya existe."""
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            producto["cantidad"] += cantidad
            print(f"✅ Se actualizó la cantidad de {nombre}. Nueva cantidad: {producto['cantidad']}")
            return
    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    print(f"🟢 Producto '{nombre}' agregado correctamente.")


def vender_producto(inventario: list, nombre: str, cantidad: int) -> None:
    """Vende cierta cantidad de un producto, si existe y hay stock."""
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                print(f"💰 Venta realizada: {cantidad} unidades de {nombre}.")
                if producto["cantidad"] == 0:
                    inventario.remove(producto)
                    print(f"⚠️ Producto '{nombre}' agotado y eliminado del inventario.")
            else:
                print(f"❌ No hay suficiente cantidad de {nombre}. Disponible: {producto['cantidad']}")
            return
    print(f"❌ Producto '{nombre}' no encontrado.")


def mostrar_inventario(inventario: list) -> None:
    """Muestra el inventario en una tabla con Rich."""
    console = Console()
    if not inventario:
        console.print("[yellow]⚠️ El inventario está vacío.[/yellow]")
        return

    tabla = Table(title="📦 Inventario Actual")
    tabla.add_column("Nombre", justify="left", style="cyan")
    tabla.add_column("Cantidad", justify="center", style="magenta")
    tabla.add_column("Precio", justify="right", style="green")

    for item in inventario:
        tabla.add_row(item["nombre"], str(item["cantidad"]), f"${item['precio']:.2f}")

    console.print(tabla)


# ============================
# PROGRAMA PRINCIPAL
# ============================

def main():
    """Interfaz principal del gestor de inventario."""
    inventario = cargar_inventario()
    console = Console()

    while True:
        console.print("\n[bold blue]=== GESTOR DE INVENTARIO ===[/bold blue]")
        console.print("1. Ver inventario")
        console.print("2. Agregar producto")
        console.print("3. Vender producto")
        console.print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            mostrar_inventario(inventario)

        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar_producto(inventario, nombre, cantidad, precio)
            guardar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Nombre del producto a vender: ")
            cantidad = int(input("Cantidad a vender: "))
            vender_producto(inventario, nombre, cantidad)
            guardar_inventario(inventario)

        elif opcion == "4":
            guardar_inventario(inventario)
            console.print("[green] Cambios guardados. Saliendo del programa...[/green]")
            break
        else:
            console.print("[red]Opción inválida. Intente de nuevo.[/red]")


if __name__ == "__main__":
    main()
