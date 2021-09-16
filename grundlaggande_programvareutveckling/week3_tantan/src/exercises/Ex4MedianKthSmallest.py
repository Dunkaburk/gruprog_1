# package exercises

#
# Even more list methods, possibly even trickier
#
def median_kth_smallest_program():
    list1 = [9, 3, 0, 1, 3, -2]

    # print(not is_sorted(list1))  # Is sorted in increasing order? No not yet!

    # sort(list1)     # Sort in increasing order, original order lost!

    print(list1 == [-2, 0, 1, 3, 3, 9])

    # print(is_sorted(list1))  # Is sorted in increasing order? Yes!

    list2 = [5, 4, 2, 1, 7, 0, -1, -4, 12]
    list3 = [2, 3, 0, 1]
    # print(median(list2) == 2)    # Calculate median of elements
    # print(median(list3) == 1.5)

    list4 = [2, 3, 0, 1, 5, 4]
    list5 = [5, 4, 2, 2, 1, 7, 4, 0, -1, -4, 0, 0, 12]
    # print(k_smallest(list4, 2) == 1)   # Second smallest is 1
    # print(k_smallest(list5, 5) == 2)   # 5th smallest is 2

    # ---------- Write methods here --------------


if __name__ == "__main__":
    median_kth_smallest_program()
