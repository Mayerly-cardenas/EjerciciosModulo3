"""Ejercicio 1: Calculadora de IMC.

Este programa calcula el Índice de Masa Corporal (IMC) de una persona
y lo interpreta según los valores estándar de salud.
"""

from rich.console import Console

console = Console()


def calcular_imc(peso: float, altura: float) -> float:
    """Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): Peso de la persona en kilogramos.
        altura (float): Altura de la persona en metros.

    Returns:
        float: Valor del IMC calculado.
    """
    return peso / (altura**2)


def interpretar_imc(imc: float) -> str:
    """Interpreta el valor del IMC según las categorías estándar.

    Args:
        imc (float): Valor del índice de masa corporal.

    Returns:
        str: Categoría correspondiente al IMC.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


def main() -> None:
    """Orquesta la ejecución del programa IMC."""
    console.print("[bold cyan]--- Calculadora de IMC ---[/bold cyan]")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = calcular_imc(peso, altura)
    resultado = interpretar_imc(imc)

    console.print(f"\nTu IMC es: [bold yellow]{imc:.2f}[/bold yellow]")
    console.print(f"Categoría: [bold green]{resultado}[/bold green]")


if __name__ == "__main__":
    main()
