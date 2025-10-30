from rich.console import Console
from rich.table import Table
import os

ARCHIVO_TAREAS = "tareas.txt"
console = Console()

def agregar_tarea(tarea: str) -> None:
    """
    Agrega una tarea al archivo de texto. Si el archivo no existe, se crea automáticamente.
    """
    with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
        archivo.write(tarea + "\n")


def ver_tareas() -> list[str]:
    """
    Lee y muestra las tareas en una tabla usando la librería rich.
    Retorna una lista con las tareas.
    """
    if not os.path.exists(ARCHIVO_TAREAS):
        console.print("[yellow]No hay tareas registradas todavía.[/yellow]")
        return []

    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        tareas = [t.strip() for t in archivo.readlines() if t.strip()]

    if not tareas:
        console.print("[yellow]El archivo está vacío.[/yellow]")
        return []

    # Crear tabla bonita
    tabla = Table(title="Lista de Tareas", show_header=True, header_style="bold cyan")
    tabla.add_column("N°", style="dim", width=5)
    tabla.add_column("Tarea", style="bold white")

    for i, tarea in enumerate(tareas, start=1):
        tabla.add_row(str(i), tarea)

    console.print(tabla)
    return tareas


def eliminar_tarea(numero: int) -> None:
    """
    Elimina una tarea del archivo según su número en la lista.
    """
    tareas = ver_tareas()
    if 0 < numero <= len(tareas):
        tareas.pop(numero - 1)
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            archivo.writelines([t + "\n" for t in tareas])
        console.print(f"[green]Tarea {numero} eliminada correctamente.[/green]")
    else:
        console.print("[red]Número de tarea inválido.[/red]")


def main():
    """
    Muestra el menú principal del gestor de tareas.
    """
    while True:
        console.print("\n[bold cyan]GESTOR DE TAREAS[/bold cyan]")
        console.print("1. Agregar tarea")
        console.print("2. Ver tareas")
        console.print("3. Eliminar tarea")
        console.print("4. Salir")

        opcion = input("\nSelecciona una opción (1-4): ")

        if opcion == "1":
            tarea = input("Escribe la tarea: ")
            agregar_tarea(tarea)
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            try:
                numero = int(input("Número de tarea a eliminar: "))
                eliminar_tarea(numero)
            except ValueError:
                console.print("[red]Por favor ingresa un número válido.[/red]")
        elif opcion == "4":
            console.print("[bold green]¡Hasta luego![/bold green]")
            break
        else:
            console.print("[red]Opción no válida. Intenta de nuevo.[/red]")


if __name__ == "__main__":
    main()
