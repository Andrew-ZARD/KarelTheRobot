"""
File: MidpointKarel.py
Name: Andrew
----------------------------
When finished, this program should leave a beeper
on the corner closest to the midpoint of 1st Street.

If 1st Street has an even number of corners,
either of the two central corners is acceptable.
Karel may use additional beepers while searching
for the midpoint, but must remove them before stopping.

The world can be of any size, and you may assume
that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *
def turn_right():# Let Karel turn left
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def main():
    """
    TODO:
    """
    turn_left()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
        turn_right()
        move()
        turn_left()
    turn_around()
    while front_is_clear():
        move()
    put_beeper()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
