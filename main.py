from operations.suma import suma
from operations.resta import resta
from operations.multiplicacion import multiplicacion
from operations.division import division

if __name__ == "__main__":

    a, b = 10, 5
    print("suma:", suma(a, b))
    print("resta:", resta(a, b))
    print("multiplicacion:", multiplicacion(a, b))
    print("division:", division(a, b))
