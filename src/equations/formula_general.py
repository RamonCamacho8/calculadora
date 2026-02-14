from src.operations.suma import sumar
from src.operations.resta import restar
from src.operations.multiplicacion import multiplicar
from src.operations.potencia import potencia
from src.operations.division import division
from src.operations.raiz_cuadrada import raiz_cuadrada


def formula_general(a: float, b: float, c: float) -> tuple:
    """Calcula las soluciones de la ecuación cuadrática ax^2 + bx + c = 0
    utilizando la fórmula general.

    Args:
        a (float): Coeficiente cuadrático.
        b (float): Coeficiente lineal.
        c (float): Término independiente.

    Returns:
        tuple: Una tupla que contiene las dos soluciones (x1, x2).
    """
    if a == 0:
        raise ValueError(
            "El coeficiente 'a' no puede ser 0 en una ecuación cuadrática."
                         )

    discriminante = restar(potencia(b, 2), multiplicar(4, multiplicar(a, c)))

    if discriminante < 0:
        raise ValueError("La ecuación no tiene soluciones reales.")

    raiz_discriminante = raiz_cuadrada(discriminante)
    denominador = multiplicar(2, a)

    x1_numerador = sumar(-b, raiz_discriminante)
    x2_numerador = restar(-b, raiz_discriminante)

    x1 = division(x1_numerador, denominador)
    x2 = division(x2_numerador, denominador)

    return (x1, x2)
