import csv
import json
from rich.console import Console

console = Console()

def leer_csv(nombre_archivo):
    """Lee los datos de un archivo CSV y devuelve una lista de diccionarios."""
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as file:
            lector = csv.DictReader(file)
            return list(lector)
    except FileNotFoundError:
        console.print(f"[red]Error:[/] No se encontró el archivo {nombre_archivo}")
        return []

def leer_json(nombre_archivo):
    """Lee los datos de un archivo JSON y devuelve un diccionario."""
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        console.print(f"[red]Error:[/] No se encontró el archivo {nombre_archivo}")
        return {}

def generar_reporte(estudiantes, cursos, archivo_salida):
    """Combina los datos y genera un reporte en texto."""
    lineas = ["REPORTE DE ESTUDIANTES Y CURSOS", "-" * 40]

    for estudiante in estudiantes:
        id_est = estudiante["id_estudiante"]
        nombre = estudiante["nombre"]
        lista_cursos = cursos.get(id_est, [])
        cursos_texto = ", ".join(lista_cursos) if lista_cursos else "No tiene cursos registrados"
        lineas.append(f"{nombre}: {cursos_texto}")

    reporte = "\n".join(lineas)

    # Mostrar en consola con rich
    console.print(f"[bold cyan]{reporte}[/bold cyan]")

    # Guardar en archivo
    with open(archivo_salida, mode='w', encoding='utf-8') as file:
        file.write(reporte)

    console.print(f"\n[green]Reporte generado correctamente en {archivo_salida}[/green]")

def main():
    estudiantes = leer_csv("estudiantes.csv")
    cursos = leer_json("cursos.json")
    generar_reporte(estudiantes, cursos, "reporte.txt")

if __name__ == "__main__":
    main()
