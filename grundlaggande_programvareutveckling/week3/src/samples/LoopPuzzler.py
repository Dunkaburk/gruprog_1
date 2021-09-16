# package samples

#
# A Puzzler, plotting a pattern
#
def loop_puzzler_program():

    # Plot a half square.
    for i in range(10):
        for j in range(i):  # j depends on i !!!
            print("X", end='')   # end='' overrides the default newline
        print("")  # print newline


if __name__ == "__main__":
    loop_puzzler_program()
