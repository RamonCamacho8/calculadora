from src.operations.potencia import potencia
import pytest


def obtener_datos_prueba():
    return [
        (2, 3, 8),
        (-2, 3, -8),
        (2, -2, 0.25),
        (5, 0, 1),
        (0, 5, 0),
        (4, 0.5, 2.0),
    ]
    

@pytest.mark.parametrize("a, e, resultado_esperado", obtener_datos_prueba())
def test_potencia(a, e, resultado_esperado):
    assert potencia(a, e) == resultado_esperado