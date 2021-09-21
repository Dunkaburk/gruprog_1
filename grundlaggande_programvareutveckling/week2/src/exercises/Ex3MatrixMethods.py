# package exercises

#  * See:
#  * - Matrices
from typing import List


def matrix_methods_program():
    matrix: List[List[int]] = [  # Hard coded test data
        [-1, 0, -5, 3],
        [6, 7, -2, 0],
        [9, -2, -6, 8],
        [0, 0, 5, -6]]

    plot(matrix)

    # TODO uncomment one section at a time and implement

    # # Return list with all negatives in m
    # negs = get_negatives(matrix)
    # print(len(negs) == 6)
    # print(negs == [-1, -5, -2, -2, -6, -6])

    # # Mark all negatives with a 1, others as 0
    # # (create matrix on the fly)
    # marked = mark_negatives([
    #             [1, -2, 3,],
    #             [-4, 5, -6,],
    #             [7, -8, 9,] ])
    # # marked should be (don't uncomment)
    # #    [ [0, 1, 0],
    # #      [1, 0, 1],
    # #      [0, 1, 0] ]
    # print(marked[0] == [0, 1, 0])
    # print(marked[1] == [1, 0, 1])
    # print(marked[2] == [0, 1, 0])

    # start_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # # Create matrix from list
    # matrix = to_matrix(start_list)
    # # matrix should be (don't uncomment)
    # # [ [1, 2, 3],
    # #   [4, 5, 6],
    # #   [7, 8, 9] ]
    # plot(matrix)  # If manual inspection
    # print(matrix[0] == [1, 2, 3])
    # print(matrix[1] == [4, 5, 6])
    # print(matrix[2] == [7, 8, 9])

    # # Sum of all directly surrounding elements to some element in matrix
    # # (not counting the element itself)
    # # NOTE: Should be possible to expand method to include more distant neighbours
    # print(sum_neighbours(matrix, 0, 0) == 11)
    # print(sum_neighbours(matrix, 1, 1) == 40)
    # print(sum_neighbours(matrix, 1, 0) == 23)
    

# -------- Write methods below this -----------------------
# TODO implement get_negatives
# TODO implement mark_negatives
# TODO implement to_matrix
# TODO implement sum_neighbours


# Utility function if you want to manually inspect the matrices
def plot(matrix):
    for row in matrix:
        print(row)


if __name__ == "__main__":
    matrix_methods_program()
