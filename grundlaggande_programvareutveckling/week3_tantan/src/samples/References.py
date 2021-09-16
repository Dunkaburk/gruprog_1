# package samples

#
# Some examples of reference variables and values vs identities (lists and for now)
#
def references_program():
    list1 = [7, 1, 0, 4, -2]
    list2 = [5, 4, 3, 2, 1]
    list3 = [5, 4, 3, 2, 1]   # Same values as list2

    print(list1 is list2)           # False, different objects
    print(list2 == list3)           # True, same values
    print(list2 is list3)           # False, same values but different objects, different identities!

    print(list2[0] == list3[0])     # True, same values
    print(list2[0] is list3[0])     # True, integers are values, not objects; same value implies same identity

    list3 = list1
    print(list1 is list3)           # True, now references exact same object, same identity - alias!

    print(list1[0] == list2[0])     # False, not same value
    print(list1[0] == list3[0])     # True, same value
    print(list3[0])                 # 7
    list1[0] = 4                    # Update list1
    print(list3[0])                 # 4 - alias problem! list3 changed when we updated list1! Same object.

    # Strings
    s1 = "Hello "
    s2 = "world"
    s3 = s1 + s2
    s1 = ""
    s2 = ""
    print(s3)  # s3 not affected when changing variables s1 and s2

    s1 = s3
    print(s1)  # s1 references same object as s3

    print(s1 is s3)                 # True, reference same object
    print(s1 == "Hello world")      # True, same text
    print(s1 is "Hello world")      # False, same characters but different objects
    # The last one gives a SyntaxWarning, since this can *never*
    # be true with a string literal - why?


if __name__ == "__main__":
    references_program()
