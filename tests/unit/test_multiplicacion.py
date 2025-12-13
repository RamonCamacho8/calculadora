from src.operations.multiplicacion import multiplicar
import pytest


def obtener_datos_prueba():
    return [
        (2, 3, 6),
        (-2, -3, 6),
        (-2, 3, -6),
        (0, 5, 0),
        (1.5, 2, 3.0),
    ]


@pytest.mark.parametrize("a, b, resultado_esperado", obtener_datos_prueba())
def test_multiplicar(a, b, resultado_esperado):
    assert multiplicar(a, b) == resultado_esperado
