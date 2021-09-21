# package exercises

#  *  Methods with list params and/or return value. Implement methods.
#  *
#  *  See:
#  *  - MathMethods
#  *  - ListMethods
def list_methods_program():
    test_list = [1, 2, 2, 5, 3, 2, 4, 2, 7]  # Hard coded test data

    # TODO uncomment one section at a time and implement

    # Count occurrences of some element in arr
    # print(count(arr, 2) == 4);      # There are four 2's
    # print(count(arr, 7) == 1);

    # Generate array with 100 elements with 25% distribution of -1's and 1's (remaining will be 0)
    # arr = generate_distribution(100, 0.25, 0.25);
    # print(count(arr, 1) == 25);
    # print(count(arr, -1) == 25);
    # print(count(arr, 0) == 50);

    # Generate array with 14 elements with 40% 1's and 30% -1's
    # arr = generate_distribution(14, 0.4, 0.3);
    # print(count(arr, 1) == 6);
    # print(count(arr, -1) == 4);

    for _i in range(10):  # Run this loop 10 times
        # Random reordering of arr, have to check by inspecting output
        # shuffle(arr);
        print(test_list)  # Does it look random?

# ---- Write methods below this ------------
# TODO implement count
# TODO implement generate_distribution
# TODO implement shuffle


if __name__ == "__main__":
    list_methods_program()