from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""
"""
An part of the extension, I made a program that allows karel to draw a STAR shape in any square world
"""

from karel.stanfordkarel import *

# pre: karel is facing east ready to build a the diagonals of a squared world
# post: karel build the diagonals and now return back and facing east again
def main():
    create_a_1st_diagonal_shape()
    turn_west_to_the_wall()
    create_a_2nd_diagonal_shape()
    karel_return_to_its_starting_point()

# pre: karel facing east at the top-most right corner
# post: karel facing east at the top-most left corner of the world
def turn_west_to_the_wall():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

# pre: karel facing east at the left-most part of the world i.e corner (1,1)
# post: karel again facing east but this time at the top-most corner of the world
def create_a_1st_diagonal_shape():
    while front_is_clear():
        if front_is_clear():
            paint_corner(BLUE)
            turn_left()
            if front_is_blocked():
                turn_left()
            else:
                move()
        turn_karel_right()
        move()
    paint_corner(BLUE)

# pre: karel facing east at the top-most left corner of the world
# post: karel is facing east blocked by wall
def create_a_2nd_diagonal_shape():
    if front_is_clear():
        paint_corner(DARK_GRAY)
        move()
        turn_karel_right()
        move()
        paint_corner(DARK_GRAY)
        move()
        while front_is_clear():
            turn_left()
            move()
            paint_corner(DARK_GRAY)
            turn_karel_right()
            move()
        turn_left()
        move()
        paint_corner(DARK_GRAY)

# pre: karel is facing east at the south-most corner
# post: karel is facing east at corner (1,1)
def karel_return_to_its_starting_point():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def turn_around():
    turn_left()
    turn_left()

def turn_karel_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
