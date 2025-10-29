"""
Ejercicio 2: Generador de Perfiles de Usuario con Argumentos Flexibles

Este módulo contiene la función crear_perfil, que genera un perfil de usuario
utilizando argumentos posicionales, *args y **kwargs.
"""

from typing import Tuple, Dict


def crear_perfil(nombre: str, edad: int, *hobbies: str, **redes_sociales: str) -> str:
    """
    Genera un perfil de usuario con nombre, edad, hobbies y redes sociales.

    Parámetros:
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario.
        *hobbies (str): Lista variable de hobbies.
        **redes_sociales (str): Redes sociales del usuario con su respectivo usuario.

    Retorna:
        str: Una cadena formateada con toda la información del perfil.
    """
    perfil = f" Perfil de {nombre} ({edad} años)\n"

    if hobbies:
        perfil += " Hobbies:\n"
        for hobby in hobbies:
            perfil += f"   - {hobby}\n"

    else:
        perfil += " Hobbies: Ninguno registrado\n"

    if redes_sociales:
        perfil += " Redes Sociales:\n"
        for red, usuario in redes_sociales.items():
            perfil += f"   - {red.capitalize()}: {usuario}\n"
    else:
        perfil += " Redes Sociales: Ninguna registrada\n"

    return perfil.strip()
