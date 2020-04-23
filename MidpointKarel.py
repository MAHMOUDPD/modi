from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""



def main():
    if front_is_clear():
        fill_whole_street_with_beepers()
        pick_beepers_at_the_ends()
        karel_move_to_the_middle_put_beeper()
    else:
        # if front of karel is blocked, put beeper and stop
        put_beeper()


# pre condition: karel is facing east
# post condition: karel is blocked by the wall facing east
def fill_whole_street_with_beepers():
    if front_is_blocked():
        put_beeper()
    else:
        move()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


# pre condition: karel is blocked by the wall while facing east
# post condition: karel continuously pick beepers at the end corners when a beeper is present

def pick_beepers_at_the_ends():
    turn_around()
    while beepers_present():
        check_presence_of_beepers()
        keep_moving()
        check_presence_of_beepers()

# pre: karel facing east when no beeper remains
# post: karel in the middle on top of beeper
def karel_move_to_the_middle_put_beeper():
    if facing_east():
        turn_around()
        move()
    if front_is_clear():
        put_beeper()
    if front_is_blocked():
        turn_around()
        move()
        put_beeper()

# pre condition: karel check if beeper present
# post condition: karel pick beeper, otherwise move until it reaches a beeper

def check_presence_of_beepers():
    if beepers_present():
        pick_beeper()
        move()
    else:
        move()
        if beepers_present():
            pick_beeper()
            move()

# pre condition: karel picked beeper
# post condition: karel continue moving until it reaches an empty corner
def keep_moving():
    while beepers_present():
        move()
    turn_around()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
