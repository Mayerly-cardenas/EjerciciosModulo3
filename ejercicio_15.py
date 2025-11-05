import json
from rich.console import Console
from rich.table import Table
from typing import List, Dict, Optional

console = Console()

# ---------- Funciones de manejo de datos ----------

def cargar_biblioteca(archivo: str) -> List[Dict]:
    """Carga los datos de la biblioteca desde un archivo JSON."""
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        console.print(f"[yellow]Archivo {archivo} no encontrado. Creando uno nuevo...[/yellow]")
        return []
    except json.JSONDecodeError:
        console.print("[red]Error: El archivo JSON está dañado o vacío.[/red]")
        return []

def guardar_biblioteca(archivo: str, datos: List[Dict]) -> None:
    """Guarda los datos de la biblioteca en el archivo JSON."""
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

# ---------- Funciones principales ----------

def prestar_libro(libro_id: str, nombre_aprendiz: str, biblioteca: List[Dict]) -> Optional[str]:
    """Marca un libro como prestado a un aprendiz."""
    for libro in biblioteca:
        if libro["libro_id"] == libro_id:
            if libro["prestado_a"] is not None:
                return f"El libro '{libro['titulo']}' ya está prestado."
            libro["prestado_a"] = nombre_aprendiz
            return f"Libro '{libro['titulo']}' prestado a {nombre_aprendiz}."
    return "Libro no encontrado."

def devolver_libro(libro_id: str, biblioteca: List[Dict]) -> str:
    """Marca un libro como disponible nuevamente."""
    for libro in biblioteca:
        if libro["libro_id"] == libro_id:
            if libro["prestado_a"] is None:
                return f"El libro '{libro['titulo']}' no estaba prestado."
            libro["prestado_a"] = None
            return f"Libro '{libro['titulo']}' devuelto correctamente."
    return "Libro no encontrado."

def buscar_libro(query: str, biblioteca: List[Dict]) -> List[Dict]:
    """Busca libros por coincidencia en el título."""
    resultados = [libro for libro in biblioteca if query.lower() in libro["titulo"].lower()]
    if resultados:
        tabla = Table(title=f"Resultados de búsqueda: '{query}'")
        tabla.add_column("ID", justify="center")
        tabla.add_column("Título", justify="left")
        tabla.add_column("Prestado a", justify="center")

        for libro in resultados:
            prestado = libro["prestado_a"] if libro["prestado_a"] else "Disponible"
            tabla.add_row(libro["libro_id"], libro["titulo"], prestado)

        console.print(tabla)
    else:
        console.print(f"[red]No se encontraron libros con '{query}'.[/red]")
    return resultados

def ver_libros_prestados(biblioteca: List[Dict]) -> List[Dict]:
    """Muestra todos los libros actualmente prestados."""
    prestados = [libro for libro in biblioteca if libro["prestado_a"]]
    if prestados:
        tabla = Table(title="Libros Prestados")
        tabla.add_column("ID", justify="center")
        tabla.add_column("Título", justify="left")
        tabla.add_column("Prestado a", justify="center")

        for libro in prestados:
            tabla.add_row(libro["libro_id"], libro["titulo"], libro["prestado_a"])

        console.print(tabla)
    else:
        console.print("[green]No hay libros prestados actualmente.[/green]")
    return prestados

# ---------- Menú interactivo ----------

def menu_principal():
    archivo = "biblioteca.json"
    biblioteca = cargar_biblioteca(archivo)

    while True:
        console.print("\n[bold cyan]=== SISTEMA DE BIBLIOTECA ===[/bold cyan]")
        console.print("1. Prestar libro")
        console.print("2. Devolver libro")
        console.print("3. Buscar libro")
        console.print("4. Ver libros prestados")
        console.print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            libro_id = input("ID del libro: ")
            nombre = input("Nombre del aprendiz: ")
            msg = prestar_libro(libro_id, nombre, biblioteca)
            console.print(msg)
        elif opcion == "2":
            libro_id = input("ID del libro: ")
            msg = devolver_libro(libro_id, biblioteca)
            console.print(msg)
        elif opcion == "3":
            query = input("Buscar título: ")
            buscar_libro(query, biblioteca)
        elif opcion == "4":
            ver_libros_prestados(biblioteca)
        elif opcion == "5":
            guardar_biblioteca(archivo, biblioteca)
            console.print("[green]Cambios guardados. ¡Hasta luego![/green]")
            break
        else:
            console.print("[red]Opción no válida.[/red]")

if __name__ == "__main__":
    menu_principal()
