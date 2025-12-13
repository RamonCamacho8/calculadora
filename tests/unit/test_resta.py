from src.operations.resta import restar
import pytest


def obtener_datos_prueba():
    return [
        (5, 3, 2),
        (-5, -3, -2),
        (-5, 3, -8),
        (0, 5, -5),
        (2.5, 1.5, 1.0),
        (0, 0, 0),
    ]


@pytest.mark.parametrize("a, b, resultado_esperado", obtener_datos_prueba())
def test_restar(a, b, resultado_esperado):
    assert restar(a, b) == resultado_esperado
