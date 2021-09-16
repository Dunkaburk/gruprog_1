# package samples
# 
#  Side effect
#
#  When an expression is evaluated it produces a value (which has a type)
#  That's the normal way but, ... some expressions, besides producing
#  a value, do something more (alter memory).
#  This is called as side effect.
#
#  Some side effects
#  - Assignments (value is "the assigned" value, side effect is memory altered)
#  - Constructing new objects (value is the new object, side effect is memory altered)
def side_effect_program():
    a = 1
    b = 2

    print(a)
    print(a := 3)     # Side effect: a updated *as an expression*, value of expression is new value
    print(a)

    print(++a)        # This is *not* an increment operator (as in e.g. Java). What is it?

    print(a := b)     # Side effect: value in b copied to a, value is b
    print(a)

    c = a = b           # Python allows us to write chained assignments
    print(f"{a} {b} {c}")

    print(get_a_number(0) - get_a_number(0) == 0)   # Or??

    d: Dog = Dog("Hercules")  # Value is ref. to Dog, technically a side effect, memory allocated
    print(d.name)


N: int = 0  # Global variable - yuck!


# Method with side effect. Not referentially transparent
def get_a_number(i):
    global N  # Global variable - yuck!
    N += 1
    return N + i


class Dog:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    side_effect_program()


