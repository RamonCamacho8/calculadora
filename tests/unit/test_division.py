from src.operations.division import division
import pytest


def obtener_datos_prueba():
    return [
        (6, 3, 2),
        (-6, -3, 2),
        (-6, 3, -2),
        (0, 5, 0),
        (5.0, 2.0, 2.5),
    ]


@pytest.mark.parametrize("a, b, resultado_esperado", obtener_datos_prueba())
def test_division(a, b, resultado_esperado):
    assert division(a, b) == resultado_esperado


def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        division(5, 0)
