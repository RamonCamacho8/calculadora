from src.operations.raiz_cuadrada import raiz_cuadrada
import pytest


def obtener_datos_prueba():
    return [
        (4, 2.0),
        (9, 3.0),
        (0, 0.0),
        (16, 4.0),
        (2.25, 1.5),
    ]


@pytest.mark.parametrize("a, resultado_esperado", obtener_datos_prueba())
def test_raiz_cuadrada(a, resultado_esperado):
    assert raiz_cuadrada(a) == resultado_esperado


@pytest.mark.parametrize("a", [-4, -9, -1])
def test_raiz_cuadrada_negativa(a):
    with pytest.raises(ValueError):
        raiz_cuadrada(a)
