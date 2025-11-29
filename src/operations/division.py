def division(a, b):
    """
    Calcula la división de dos números.

    Args:

        x: El primer número (flotante).
        y: El segundo número (flotante).

    Returns:
        La división de x y y.
    """
    if b == 0:
        raise ZeroDivisionError("El denominador no puede ser cero")
    return a / b
