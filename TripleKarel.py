from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    walls_of_1st_building()
    walls_of_2nd_building()
    walls_of_3rd_building()

# pre: karel is facing west about to start painting
# post: karel paint the 1st block successfully
def walls_of_1st_building():
    for i in range(3):
        paint_walls_of_the_blocks()
    turn_around()
    move()

# pre: karel is facing south
# post: karel painted the wall and now facing east
def walls_of_2nd_building():
    for i in range(3):
        paint_walls_of_the_blocks()
    turn_around()
    move()

# pre: karel is now facing east
# post: karel painted the 3rd wall and facing west as expected
def walls_of_3rd_building():
    for i in range(3):
        paint_walls_of_the_blocks()
    turn_around()
    move()
    turn_left()

# pre: NONE
# post: karel paint the exterior of the block
def paint_walls_of_the_blocks():
    while left_is_blocked():
        put_beeper()
        move()
    turn_left()
    move()

def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
