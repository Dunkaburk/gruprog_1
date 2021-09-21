# package samples

# /*
#  *  A matrix is 2 dimensional array, an array of arrays
#  *
#  *  Must use 2 index: First is row and second is col
#  *  As usual index starts on 0.
#  *
#  *  NOTE: We normally use square matrices!
#  */
def matrices_program():
    # Declare and initialize matrix
    matrix = [                  # A list of lists
        [1, 2, 3],         # matrix[0] = first row (first sub list)
        [4, 5, 6],         # matrix[1]
        [7, 8, 9],         # matrix[2]
        ]

    print(matrix[0][2] == 3)   # Row 0, col 2
    # print(matrix[1][3] == 6)   # Exception, index out of bounds

    matrix[1][2] = 99    # Assign

    r = 2
    c = 2
    matrix[r][c - 1] = -1    # Assign using variables

    # Traversing. Must use nested loops
    for row in matrix:
        for element in row:
            print(element)

    # Traverse and update
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1
    plot_matrix(matrix)

    # Create new matrices in program
    matrix = [[0] * 4] * 4      # New 4x4 matrix with 0's
    plot_matrix(matrix)

    matrix = [    # New 2x2 initialized with values
        [11, 12],
        [21, 22]
        ]
    plot_matrix(matrix)

    s = sum_matrix(matrix)
    print(s)

    the_copy = copy(matrix)  # Make a copy
    plot_matrix(the_copy)

    
# --------- Methods ----------------------
def sum_matrix(matrix):
    the_sum = 0
    for row in matrix:
        for element in row:
            the_sum += element
    return the_sum
    

def copy(matrix):
    # Create the copy matrix
    the_copy = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element)
        the_copy.append(new_row)
    return the_copy
    

def plot_matrix(matrix):
    # Traversing
    for row in matrix:
        # Row is a list
        print(row)


if __name__ == "__main__":
    matrices_program()
