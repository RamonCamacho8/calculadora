from src.operations.suma import sumar
import pytest


def obtener_datos_prueba():
    return [
        (2, 3, 5),
        (-2, -3, -5),
        (-2, 3, 1),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ]


@pytest.mark.parametrize("a, b, resultado_esperado", obtener_datos_prueba())
def test_sumar(a, b, resultado_esperado):
    assert sumar(a, b) == resultado_esperado
