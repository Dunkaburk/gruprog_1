from typing import List
from enum import Enum, auto
from random import *

import pygame as pg

matrix = [[0, 1, 2], [4, 9, 8], [2, 1, 1]]

list_1 = [3, 4, 5, 7, 1, 2, 1, 5, 9, 1]



def switch_unsatisfied_agents(unsatisfied_agents, matrix):
    
    shuffle(unsatisfied_agents)

    while len(unsatisfied_agents) > 0:
        random_row = randint(0, 2)
        random_index = randint(0, 2)

        if matrix[random_row][random_index] == 1:
            matrix[random_row][random_index] = unsatisfied_agents[0]
            unsatisfied_agents.pop(0)

    return matrix


switch_unsatisfied_agents(list_1, matrix)
print(matrix)
print("List_1", list_1)