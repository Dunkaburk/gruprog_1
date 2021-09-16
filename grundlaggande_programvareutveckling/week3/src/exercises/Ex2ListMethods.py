# package exercises

#
#  Some harder list methods
#
def list_methods_program():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]

    # # Rotate all elements in the arr k steps to the right (in a circular fashion)
    # # Assume arr.length > 0. NOTE: Original array changed!
    # rotate(list1, 3)
    # print(list1 == [6, 7, 8, 1, 2, 3, 4, 5])
    # rotate(list1, 0)
    # print(list1 == [6, 7, 8, 1, 2, 3, 4, 5])
    # rotate(list1, len(list1))
    # print(list1 == [6, 7, 8, 1, 2, 3, 4, 5])

    # # Same as above but here we have a return value
    # r_list = [1, 2, 3, 4, 5]
    # r_list = rotate2([1, 2, 3, 4, 5], 2)  # Return value instead of rotating in place!
    # print(r_list == [4, 5, 1, 2, 3])
    # r_list = rotate2([1, 2, 3, 4, 5], 5)
    # print(r_list == [1, 2, 3, 4, 5])

    list2 = [1, 2, 2, 3, 3]   # All sorted in increasing order
    list3 = [1, 2, 3, 4, 5]
    list4 = [1, 1, 1, 1, 1, 1]
    list5 = [1]

    # # Remove all duplicates from list2, ... (original unchanged, copy created)
    # # NOTE: Assume list is sorted in increasing order and length > 0
    # print(remove_duplicates(list2) == [1, 2, 3])
    # print(list2 == [1, 2, 2, 3, 3])   # list2 unchanged!
    # print(remove_duplicates(list3) == [1, 2, 3, 4, 5])
    # print(remove_duplicates(list4) == [1])
    # print(remove_duplicates(list5) == [1])

    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    # Use fact that array is sorted to search efficiently
    # print(search(list1, 1) == 0)
    # print(search(list1, 3) == 2)
    # print(search(list1, 8) == 7)

# -------------- Methods --------------------------
# TODO implements methods here


if __name__ == "__main__":
    list_methods_program()
