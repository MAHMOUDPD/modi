from karel.stanfordkarel import *
"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


# start the program
def main():
    move()
    turn_karel_right()
    move()
    turn_left()
    move()
    move()
    pick_beeper()
    turn_karel_right()
    retun_home()


# make karel turn right i.e 180 degrees
def turn_karel_right():
    for i in range(3):
        turn_left()


# pre: karel picked up a beeper
# post: karel returns to its initial position facing east

def retun_home():
    turn_karel_right()
    for i in range(3):
        move()
    turn_karel_right()
    move()
    turn_karel_right()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
