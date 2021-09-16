# package exercises

# from multipledispatch import dispatch

# See:
# - Overloading
#
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age  = age


def overload_methods_program():
    # TODO write a swap method that makes all the following print True
    list1 = [1, 2]
    list2 = [2, 1]
    swap(list1)
    print(list1 == list2)

    d1 = Dog("Maximus", 10)
    d2 = Dog("Hercules", 12)
    swap(d1, d2)
    d_str = f"{d1.name} ({d1.age}) and {d2.name} ({d2.age})"
    print(d_str == "Hercules (10) and Maximus (12)")

    unit1 = [1]
    unit2 = [2]
    swap(unit1, unit2)
    print(unit1 + unit2 == list2)


# ---- Implement swap() function below
def swap(*args):
    pass


if __name__ == "__main__":
    overload_methods_program()
