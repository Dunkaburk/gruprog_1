from typing import List
from enum import Enum, auto
from random import *

import pygame as pg

list = [0, 1, 2]

list_1 = [3, 4, 5]


shuffle(list)


matrix_1 = [[0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15]]


def get_neighbours(matrix, row, column):
    neighbours = []
    for i in [-1, 1]:
        if row + i >= 0 and row + i < len(matrix):
            neighbours.append(matrix[row + i][column])
        if column + i >= 0 and column + i < len(matrix):
            neighbours.append(matrix[row][column + i])
        if row + i >= 0 and column - i >= 0 and row + i < len(matrix) and column - i < len(matrix):
            neighbours.append(matrix[row + i][column - i])
        if row + i >= 0 and column + i >= 0 and row + i < len(matrix) and column + i < len(matrix):
            neighbours.append(matrix[row + i][column + i])
    return neighbours


    
print ("matrix:", get_neighbours(matrix_1, 1, 0))
    