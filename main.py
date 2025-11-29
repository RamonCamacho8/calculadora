from src.operations.suma import sumar
from src.operations.resta import restar
from src.operations.multiplicacion import multiplicar
from src.operations.division import division
from src.operations.potencia import potencia

if __name__ == "__main__":

    a, b = 10, 5
    print("suma:", sumar(a, b))
    print("resta:", restar(a, b))
    print("multiplicacion:", multiplicar(a, b))
    print("division:", division(a, b))
    print("potencia:", potencia(a, b))
