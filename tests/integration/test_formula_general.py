from src.equations.formula_general import formula_general
import pytest


def obtener_datos_prueba():
    return [
        (1, -3, 2, (2.0, 1.0)),
        (1, 2, 1, (-1.0, -1.0)),
        (1, -4, 4, (2.0, 2.0)),
        (1, 0, -4, (2.0, -2.0)),
        (2, -7, 3, (3.0, 0.5)),
        (0.5, -1.5, 1, (2.0, 1.0)),
    ]


@pytest.mark.parametrize("a, b, c, resultado_esperado", obtener_datos_prueba())
def test_formula_general(a, b, c, resultado_esperado):
    assert formula_general(a, b, c) == resultado_esperado


def test_formula_general_a_cero():
    with pytest.raises(ValueError):
        formula_general(0, 2, 1)


def test_formula_general_sin_solucion_real():
    with pytest.raises(ValueError):
        formula_general(1, 1, 1)
