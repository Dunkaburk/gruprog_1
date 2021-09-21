# package samples

from enum import Enum


# Enum (enumeration) is a type for some small set of values (a class type).
# All values that belong to type is explicitly written out when enum declared
# (so set must be small). By convention upper case is used for the values,
# since they represent constants.
#
# Enums are used because they are type safe (using String or int for days
# is not safe, i.e. can't catch misspellings or invalid numbers)
class WeekDay(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7  # List all values that belong to type


def use_enum_program():
    d1 = WeekDay.FRI  # Declare variable of enum type and assign value
    d2 = WeekDay(3)  # d2 = Wednesday

    print(d1 == d2)  # False
    d3 = WeekDay.WED
    print(d2 == d3)  # True

    print(d1.value)  # Friday is day 5
    print(d2.name)   # name is Wed

    # Iterate through the list of possible values
    for day in WeekDay:  # Yes, the class itself is iterable!
        print(day)       # Note the difference between print(day) and print(day.name)


if __name__ == "__main__":
    use_enum_program()
