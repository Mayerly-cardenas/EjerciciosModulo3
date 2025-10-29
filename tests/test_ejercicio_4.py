import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ejercicio_4 import aplicar_validador, es_email_valido, es_mayor_a_10


def test_validador_emails_validos():
    datos = ["usuario@gmail.com", "correo@empresa.com", "invalido@", "@sininicio.com", "normal@hotmail.es"]
    resultado = aplicar_validador(datos, es_email_valido)
    assert resultado == ["usuario@gmail.com", "correo@empresa.com", "normal@hotmail.es"]


def test_validador_numeros_mayores_a_10():
    numeros = [5, 11, 20, 10, 3, 15]
    resultado = aplicar_validador(numeros, es_mayor_a_10)
    assert resultado == [11, 20, 15]


def test_lista_vacia():
    datos = []
    resultado = aplicar_validador(datos, es_email_valido)
    assert resultado == []


def test_todos_invalidos():
    datos = ["sinarroba", "termina.", "@inicio"]
    resultado = aplicar_validador(datos, es_email_valido)
    assert resultado == []
