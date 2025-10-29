"""
BLOQUE 1
Ejercicio 1: Refactorización de Calculadora de IMC

"""


from rich.console import Console

console = Console()

def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): Peso de la persona en kilogramos.
        altura (float): Altura de la persona en metros.

    Returns:
        float: Valor del IMC.
    """
    return peso / (altura ** 2)


def interpretar_imc(imc: float) -> str:
    """
    Interpreta el resultado del IMC según los valores estándar.

    Args:
        imc (float): Valor calculado del IMC.

    Returns:
        str: Clasificación del IMC.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"
