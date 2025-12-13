def raiz_cuadrada(numero):
    """
    Calcula la raíz cuadrada de un número.

    :param numero: Número del cual se desea calcular la raíz cuadrada.
    :return: Raíz cuadrada del número.
    """
    if numero < 0:
        raise ValueError(
            "No se puede calcular la raíz cuadrada de un número negativo."
            )
    return numero ** 0.5
