# package exercises

#
#  Some theory mostly about references and identity
#
#  See
#  - References
#  - Overloading
from typing import List


class Player:
    def __init__(self, name):
        self.name = name


def theory_program():
    # # 1. What will happen below when you run? Will any errors occur? Why?
    # i: int = 1
    # ch: str = '1'
    # d: float = 1.0
    #
    # i = d
    # i = ch
    # ch = i
    # ch = d
    # d = i
    # d = ch
    # print(d)
    #
    # i = int(d)
    # i: float = d
    # print(i)

    # # 2. Uncomment and run.  What will be printed. Explain! ---------
    # i1 = [1, 2, 3]
    # i2 = [10, 11, 12, 13, 14, 15]
    # i3 = i1
    #
    # print(i3[1])
    # i3 = i2
    # print(i3[1])
    # i1 = i2
    # print(i3[1])
    # i3 = i1
    # i1[1] = 21
    # print(i3[1])

    # 3. What will be printed. Explain! (methods below) ----------------
    # a = 1
    # b = 2
    # swap_int(a, b)
    # print(f"{a}, {b}")
    #
    # a_list = [1, 2]
    # swap_list(a_list)
    # print(a_list)
    #
    # p1: Player = Player("olle")
    # p2: Player = Player("fia")
    #
    # swap_player(p1, p2)
    # print(p1.name + ", " + p2.name)

    # # 4. What will be printed. Explain! Methods below ----------------
    # a1: List[int] = get_list()
    # a2: List[int] = get_list()
    #
    # print(len(a1) == len(a2))
    # print(a1[0] == a2[0])
    # print(a1 == a2)
    # print(a1 is a2)

    # 5. What will happen when the next line is run? Why? (methods below)
    # print(pick_one(1, 1))
    pass


# ---------- Some methods used ---------------------------
def swap_int(a: int, b: int):
    tmp: int = a
    a = b
    b = tmp


def swap_list(a: List[int]):
    tmp: int = a[0]
    a[0] = a[1]
    a[1] = tmp


def swap_player(p1: Player, p2: Player):
    tmp: str = p1.name
    p1.name = p2.name
    p2.name = tmp


def get_list():
    the_list = [1, 2, 3]
    return the_list


def pick_one(x, y):
    return x


def pick_one(a, b, c):
    return b


if __name__ == "__main__":
    theory_program()
