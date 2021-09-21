# package samples

# math is the python API for numerical calculations
from math import *


def math_program():
    f_val = 2.1

    print(f"Square root {sqrt(f_val)}")
    print(f"Square {pow(f_val, 2)}")
    print(f"Floor {floor(f_val)}")
    print(f"Ceil {ceil(f_val)}")
    print(f"Round {round(f_val)}")
    # etc. many more ... type math. (dot) and they will show up ...

    print(pi)  # Declared in Math library

    # Comparing floats
    f1 = 1.0 - 0.7 - 0.3  # ~= 0.0
    f2 = 1.0 - 0.6 - 0.4  # ~= 0.0
    print(f1 == f2)  # False!! Rounding error!

    print(abs(f1 - f2))  # How large is the rounding error?

    # Pythagoras ... (nested calls)
    print(sqrt(pow(3, 2) + pow(4, 2)) == 5)


if __name__ == "__main__":
    math_program()
