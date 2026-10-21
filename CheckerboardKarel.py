"""
File: CheckerboardKarel.py
Name: Andrew
----------------------------
When finished, this program should
draw a checkerboard pattern using
beepers, as described in Assignment 1.

The solution should work correctly
for all of the sample worlds provided
in the starter folder.
"""

from karel.stanfordkarel import *

def turn_right():# Let Karel turn left
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def fill_one_row():
    while front_is_clear():
        if front_is_clear():
            put_beeper()
            move()
            if front_is_clear():
                move()
    turn_around()
    if not front_is_clear():
        put_beeper()
        turn_around()
    else:
        move()
        turn_around()
        if  on_beeper():
            move()
        else:
            move()
            put_beeper()

def go_back_Origin():
    #go back origin of  a row and let karel facing east
    turn_around()
    while front_is_clear():
        move()
    turn_around()



def main():
    """
      Paint the world as a checkerboard, one row at a time.
      Each row starts at its left end; the first cell of the next row
      is the opposite of the first cell of the current row.
      """
    fill_one_row()
    go_back_Origin()
    while left_is_clear():
        if on_beeper():
            turn_left()
            move()
            turn_right()
            move()
            fill_one_row()
            go_back_Origin()
        else:
            turn_left()
            move()
            turn_right()
            fill_one_row()
            go_back_Origin()






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
