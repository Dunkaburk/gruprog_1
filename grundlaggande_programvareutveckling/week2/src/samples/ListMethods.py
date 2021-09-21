# package samples

def list_methods_program():
    my_list = [1, 2, 3, 4, 5]

    print(sum_list(my_list) == 15)  # Sum all elements in array

    print(find(my_list, 4) == 3)  # Value 4 is at index 3
    print(find(my_list, 99) == -1)  # Not found

    print(find_min(my_list) == 1)  # Min value

    zero_it(my_list)  # Set all values to 0
    print(my_list == [0, 0, 0, 0, 0])

    my_list = generate_list(4, 9)  # Generate array with given value for all variables
    print(my_list == [9, 9, 9, 9])


# ---- Methods ---------------------
def sum_list(in_list):
    s = 0
    for element in in_list:
        s += element
    return s


# Return index (an int) to possibly found value.
def find(in_list, value):
    for i in range(len(in_list)):
        if in_list[i] == value:
            return i
    return -1  # Not found!


# Find min value in (non-empty) list
def find_min(in_list):
    min_value = in_list[0]  # Assume first is min ...
    for element in in_list:
        if element < min_value:
            min_value = element
    return min_value


# Set all elements to zero
# NOTE: The parameter is a reference i.e. we will change the
# original object outside of the method! So no return required.
def zero_it(in_list):
    for i in range(len(in_list)):
        in_list[i] = 0

    # Method to generate a list


def generate_list(size, value):
    new_list = []
    for _i in range(size):
        new_list.append(value)
    return new_list


if __name__ == "__main__":
    list_methods_program()
