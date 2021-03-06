from typing import List
from enum import Enum, auto
from random import *
from math import *
import pygame as pg


#  Program to simulate segregation.
#  See : http:#nifty.stanford.edu/2014/mccown-schelling-model-segregation/
#

# Enumeration type for the Actors
class Actor(Enum):
    BLUE = auto()
    RED = auto()
    NONE = auto()  # NONE used for empty locations


# Enumeration type for the state of an Actor
class State(Enum):
    UNSATISFIED = auto()
    SATISFIED = auto()
    NA = auto()  # Not applicable (NA), used for NONEs


World = List[List[Actor]]  # Type alias

SIZE = 100


def neighbours():
    pg.init()
    model = NeighborsModel(SIZE)
    _view = NeighboursView(model)
    model.run()


class NeighborsModel:
    # Tune these numbers to test different distributions or update speeds
    FRAME_RATE = 200  # Increase number to speed simulation up
    DIST = [0.4, 0.4, 0.2]  # % of RED, BLUE, and NONE
    THRESHOLD = 0.7  # % of surrounding neighbours that should be like me for satisfaction

    size = SIZE

    # ########### These following two methods are what you're supposed to implement  ###########
    # In this method you should generate a new world
    # using randomization according to the given arguments.
    @staticmethod
    def __create_world(size) -> World:
        # TODO Create and populate world according to self.DIST distribution parameters

        distributed_list = create_dist_list()
        brave_new_world = dist_list_into_matrix(distributed_list)
        return brave_new_world

    # This is the method called by the timer to update the world
    # (i.e move unsatisfied) each "frame".
    def __update_world(self):
        none_list = self.get_none_actor_index()
        unsatisfied_actors = self.pop_unsatisfied_actors()
        self.insert_unsatisfied_actors(none_list,unsatisfied_actors)
        


    # ########### the rest of this class is already defined, to handle the simulation clock  ###########
    def __init__(self, size):
        self.world: World = self.__create_world(size)
        self.observers = []  # for enabling discoupled updating of the view, ignore

    def run(self):
        clock = pg.time.Clock()
        running = True
        while running:
            running = self.__on_clock_tick(clock)
        # stop running
        print("Goodbye!")
        pg.quit()

    def __on_clock_tick(self, clock):
        clock.tick(self.FRAME_RATE)  # update no faster than FRAME_RATE times per second
        self.__update_and_notify()
        return self.__check_for_exit()

    # What to do each frame
    def __update_and_notify(self):
        self.__update_world()
        self.__notify_all()

    @staticmethod
    def __check_for_exit() -> bool:
        keep_going = True
        for event in pg.event.get():
            # Did the user click the window close button?
            if event.type == pg.QUIT:
                keep_going = False
        return keep_going

    # Use an Observer pattern for views
    def add_observer(self, observer):
        self.observers.append(observer)

    def __notify_all(self):
        for observer in self.observers:
            observer.on_world_update()


    def insert_unsatisfied_actors(self, none_index_list, unsatisfied_agents):
        shuffle(unsatisfied_agents)
        shuffle(none_index_list)
        while len(none_index_list)-1 > 0 and len(unsatisfied_agents) - 1 > 0:
            self.world[none_index_list[0][0]][none_index_list[0][1]] = unsatisfied_agents.pop(0)
            none_index_list.pop(0)
        

            # random_row = randrange(0, self.size - 1)
            # random_index = randrange(0, self.size - 1)

            # if self.world[random_row][random_index] == Actor.NONE:
            #     self.world[random_row][random_index] = unsatisfied_agents[0]
            #     unsatisfied_agents.pop(0)


    def get_none_actor_index(self):
            list_of_none_index = []
            for row in range(self.size):
                for col in range(self.size):
                    if self.world[row][col] == Actor.NONE:
                        index_of_none = []
                        index_of_none.append(row)
                        index_of_none.append(col)
                        list_of_none_index.append(index_of_none)                        
            return list_of_none_index

    def pop_unsatisfied_actors(self):
        unsatisfied_list = []
        for row in range(self.size):
            for column in range(self.size):
                current_actor = self.world[row][column]
                if current_actor != Actor.NONE:
                    if self.check_if_unsatisfied(current_actor, self.world, row, column):
                        self.world[row][column] = Actor.NONE
                        unsatisfied_list.append(current_actor)
        return unsatisfied_list

    def check_if_unsatisfied(self, current, world, row, column):
        neighbours = get_neighbours(world, row, column)
        number_of_similar = count(neighbours, current)
        number_of_none = count(neighbours, Actor.NONE)
        return number_of_similar < ceil(self.THRESHOLD * (len(neighbours)-number_of_none))





def create_dist_list():
    dist_list = []
    dist_list = add_actors(Actor.RED, NeighborsModel.DIST[0]) + add_actors(Actor.BLUE, NeighborsModel.DIST[1]) + add_actors(Actor.NONE, NeighborsModel.DIST[2])
    shuffle(dist_list)

    return dist_list


def add_actors(actor_color, distribution):
    actor_amount = round((NeighborsModel.size ** 2) * distribution)
    dist_list = []
    for element in range(actor_amount):
        dist_list.append(actor_color)

    return dist_list



def dist_list_into_matrix(dist_list):
    game_matrix = [[0 for row in range(NeighborsModel.size)] for col in range(NeighborsModel.size)]
    for position in range(len(dist_list)):
        game_matrix[position // NeighborsModel.size][position % NeighborsModel.size] = dist_list[position]

    return game_matrix


def get_neighbours(matrix, row, column):
    neighbours = []
    for i in [-1, 1]:
        if is_valid_location(NeighborsModel.size, row + i, column):
            neighbours.append(matrix[row + i][column])
        if is_valid_location(NeighborsModel.size, row, column + i):
            neighbours.append(matrix[row][column + i])
        if is_valid_location(NeighborsModel.size, row + i, column - i):
            neighbours.append(matrix[row + i][column - i])
        if is_valid_location(NeighborsModel.size, row + i, column + i):
            neighbours.append(matrix[row + i][column + i])
    return neighbours


    

    

# ---------------- Helper methods ---------------------

# Check if inside world
def is_valid_location(size: int, row: int, col: int):
    return 0 <= row < size and 0 <= col < size


# ------- Testing -------------------------------------

# Here you run your tests i.e. call your logic methods
# to see that they really work
def test():
    # A small hard coded world for testing
    test_world = [
        [Actor.RED, Actor.RED, Actor.NONE],
        [Actor.NONE, Actor.BLUE, Actor.NONE],
        [Actor.RED, Actor.NONE, Actor.BLUE]
    ]

    th = 0.5  # Simpler threshold used for testing

    dist = [0.004, 0.004, 0.92]

    size = len(test_world)
    print(is_valid_location(size, 0, 0))
    print(not is_valid_location(size, -1, 0))
    print(not is_valid_location(size, 0, 3))
    print(is_valid_location(size, 2, 2))

    
    print(get_neighbours(test_world, 0, 0) == [Actor.NONE, Actor.RED, Actor.BLUE])
    print((add_actors(Actor.BLUE, dist[0])) == [Actor.BLUE, Actor.BLUE, Actor.BLUE, Actor.BLUE])
    print((check_satisfaction(th, size, test_world)) == [Actor.BLUE])

    
def check_satisfaction(th, size, world):
        unsatisfied_list = []
        for row in range(size):
            for column in range(size):
                current_actor = world[row][column]
                if current_actor != Actor.NONE:
                    neighbours = get_neighbours(world, row, column)
                    number_of_similar = count(neighbours, current_actor)
                    number_of_none = count(neighbours, Actor.NONE)
                    if number_of_similar < ceil(th * (len(neighbours)-number_of_none)):
                        world[row][column] = Actor.NONE
                        unsatisfied_list.append(current_actor)
        return unsatisfied_list





# Helper method for testing
def count(a_list, to_find):
    the_count = 0
    for a in a_list:
        if a == to_find:
            the_count += 1
    return the_count


# ###########  NOTHING to do below this row, it's pygame display stuff  ###########
# ... but by all means have a look at it, it's fun!
class NeighboursView:
    # static class variables
    WIDTH = 700  # Size for window
    HEIGHT = 700
    MARGIN = 50

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    # Instance methods

    def __init__(self, model: NeighborsModel):
        pg.init()  # initialize pygame, in case not already done
        self.dot_size = self.__calculate_dot_size(len(model.world))
        self.screen = pg.display.set_mode([self.WIDTH, self.HEIGHT])
        self.model = model
        self.model.add_observer(self)

    def render_world(self):
        # # Render the state of the world to the screen
        self.__draw_background()
        self.__draw_all_actors()
        self.__update_screen()

    # Needed for observer pattern
    # What do we do every time we're told the model had been updated?
    def on_world_update(self):
        self.render_world()

    # private helper methods
    def __calculate_dot_size(self, size):
        return max((self.WIDTH - 2 * self.MARGIN) / size, 2)

    @staticmethod
    def __update_screen():
        pg.display.flip()

    def __draw_background(self):
        self.screen.fill(NeighboursView.WHITE)

    def __draw_all_actors(self):
        for row in range(len(self.model.world)):
            for col in range(len(self.model.world[row])):
                self.__draw_actor_at(col, row)

    def __draw_actor_at(self, col, row):
        color = self.__get_color(self.model.world[row][col])
        xy = self.__calculate_coordinates(col, row)
        pg.draw.circle(self.screen, color, xy, self.dot_size / 2)

    # This method showcases how to nicely emulate 'switch'-statements in python
    @staticmethod
    def __get_color(actor):
        return {
            Actor.RED: NeighboursView.RED,
            Actor.BLUE: NeighboursView.BLUE
        }.get(actor, NeighboursView.WHITE)

    def __calculate_coordinates(self, col, row):
        x = self.__calculate_coordinate(col)
        y = self.__calculate_coordinate(row)
        return x, y

    def __calculate_coordinate(self, offset):
        x: float = self.dot_size * offset + self.MARGIN
        return x


if __name__ == "__main__":
    neighbours()
    
    #test()
