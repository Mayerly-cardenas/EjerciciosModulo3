import csv
from rich.console import Console
from rich.table import Table

console = Console()

def analizar_csv(nombre_archivo: str, columna: str) -> dict:
    """
    Analiza una columna numérica de un archivo CSV que contiene datos de estudiantes.

    Parámetros:
        nombre_archivo (str): Nombre del archivo CSV a leer.
        columna (str): Nombre de la columna numérica que se desea analizar (por ejemplo, 'edad' o 'calificación').

    Retorna:
        dict: Diccionario con los valores de promedio, máximo y mínimo.
              Ejemplo: {"promedio": 25.3, "máximo": 30, "mínimo": 20}

    Conceptos aplicados:
        - Manejo de archivos CSV con csv.DictReader
        - Conversión de tipos
        - Uso de la librería rich para mostrar resultados en formato tabla
    """
    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            valores = []

            for fila in lector:
                try:
                    valor = float(fila[columna])
                    valores.append(valor)
                except (ValueError, KeyError):
                    continue  # Ignora filas con datos no válidos o faltantes

        if not valores:
            console.print("[red]⚠️ No se encontraron valores numéricos válidos en esa columna.[/red]")
            return {}

        resultado = {
            "promedio": sum(valores) / len(valores),
            "máximo": max(valores),
            "mínimo": min(valores)
        }

        # Mostrar los resultados en tabla con rich
        tabla = Table(title=" Resultados del Análisis CSV")
        tabla.add_column("Estadística", style="cyan", justify="center")
        tabla.add_column("Valor", style="magenta", justify="center")

        for clave, valor in resultado.items():
            tabla.add_row(clave.capitalize(), f"{valor:.2f}")

        console.print(tabla)
        return resultado

    except FileNotFoundError:
        console.print(f"[red] Error: El archivo '{nombre_archivo}' no existe.[/red]")
        return {}
    except Exception as e:
        console.print(f"[red] Error inesperado: {e}[/red]")
        return {}


def main():
    """
    Función principal que solicita al usuario un archivo CSV y una columna a analizar.
    """
    console.print("[bold green]=== ANALIZADOR DE DATOS CSV ===[/bold green]")
    nombre_archivo = input("Ingrese el nombre del archivo CSV (por ejemplo: estudiantes.csv): ")
    columna = input("Ingrese el nombre de la columna a analizar (por ejemplo: calificación): ")

    analizar_csv(nombre_archivo, columna)


if __name__ == "__main__":
    main()
