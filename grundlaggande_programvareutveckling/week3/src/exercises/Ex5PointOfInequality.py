# package exercises

#
# Finding point of inequality in any type of array, i.e. where they differ
# Question: What is the *type* of the parameters for the diff_index function?
# See:
# - Overloading
from typing import List


def point_of_inequality_program():
    a0: List[int] = [1, 2]
    a1: List[int] = [1, 2, 3, 4, 5]
    a2: List[int] = [1, 2, 33, 4, 5]
    d1: List[float] = [1.0, 2, 33, 4.5, 6.7]
    d2: List[float] = [1.0, 2, 33, 4.5, 6.711]
    s1: List[str] = ["a", "b", "c", "d", "e"]
    s2: List[str] = ["a", "bb", "c", "d", "e"]

    # All should print true
    print(diff_index(a1, a2) == 2)   # First index from left where they differ
    print(diff_index(a1, a1) == -1)  # No difference
    print(diff_index(a0, a1) == -1)
    print(diff_index(d1, d2) == 4)
    print(diff_index(s1, s2) == 1)


# ----------- Method(s) -----------------------
# What is the *type* of l1 and l2? Why?
def diff_index(l1, l2):
    pass
