# package samples

# # NOTE: This import will require you to install the library
# from multipledispatch import dispatch


#
# Overloading = Different functions/methods may have same name
# Allowed only if the parameter list is different (types and/or number of args).
#
# Typical usage: Need to do same operation on arguments with different types
#
def overload_program():
    # Uncommenting line 16 will give an error, since the *last* definition of find_max_int()
    # takes three arguments, not two (but even PyCharm is fooled here!)
    # print(find_max_int(3, 5))

    print(find_max_int(3, 5, 7))

    print(find_max_int_two(2, 4))
    print(find_max_int_three(2, 4, 6))
    print(find_max_int_overload(7, 9))
    print(find_max_int_overload(6, 8, 10))

    # # Uncomment this, and the methods at the end of the file,
    # # if you've installed the multipledispatch library
    # print(find_max(11, 12))
    # print(find_max(13, 14, 15))
    # print(find_max("hello", "hej"))


# -------- Methods ----------------------
# Find max of two ints
def find_max_int(i: int, j: int):
    return i if i > j else j    
    # An if *expression* i.e. a result is created
    # If true return i else j
    # The (normal) if *statement* doesn't return anything!


# Alt. for the above using if-statement
# This actually overwrites the previous definition
def find_max_int(i: int, j: int):
    if i > j:
        return i
    return j


# This ALSO overwrites the previous definitions
def find_max_int(i: int, j: int, k: int):
    # Psst - Can you write this in a more elegant way?
    if i > j:
        if i > k:
            return i
        return k
    if j > k:
        return j
    return k


# Alright, let's make another attempt, with different names
def find_max_int_two(i, j):
    return i if i > j else j


def find_max_int_three(i, j, k):
    h = i if i > j else j
    return h if h > k else k


# Python lets us write a method that take *any* number of arguments,
# by putting a * in front of the parameter name; then we get any
# arguments as a list:
def find_max_int_overload(*args):
    # args is now a variable pointing to a list holding all the arguments
    if len(args) == 2:
        return find_max_int_two(args[0], args[1])
    elif len(args) == 3:
        return find_max_int_three(args[0], args[1], args[2])
    else:
        raise NotImplementedError


# But now what if we want to use other types than ints?
# Of course we could actually use find_max_int_two() for other types
# than ints, despite the name we've given it,
# since all it relies on is the ability to compare values using > .
# But what if we want to use a different *way* of comparison for strings,
# say like the following?
def find_max_str(s1: str, s2: str):
    return s1 if len(s1) > len(s2) else s2


# So we can do an even uglier trick, checking the type of the arguments
# to know which other method to dispatch to. This is not scalable...
def find_max_overload(*args):
    t = type(args[0])
    if t == str:
        find_max_str(args[0], args[1])
    elif t == int:
        find_max_int_overload(args)
    else:
        raise NotImplementedError


# # For a less ugly and more scalable version, we
# # can automate the process of choosing method to run based on
# # what arguments are given, giving us true overloading of function names,
# # using so called *decorators*, here implemented from the multipledispatch
# # library. We haven't gotten this far in the course yet though,
# # and it's not part of what we require you to know for a passing
# # grade. I still include them for completeness, and we'll talk about them
# # a bit towards the end of the course.
# @dispatch(int, int)
# def find_max(i, j):
#     return i if i > j else j
#
#
# @dispatch(int, int, int)
# def find_max(i, j, k):
#     h = i if i > j else j
#     return h if h > k else k
#
#
# @dispatch(str, str)
# def find_max(s1, s2):
#     return s1 if len(s1) > len(s2) else s2


if __name__ == "__main__":
    overload_program()
