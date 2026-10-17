"""
File: StoneMasonKarel.py
Name: Andrew
--------------------------------
At the start, this program does nothing.

Your task is to add the necessary code to guide Karel
to build stone columns that are five beepers tall
on each appropriate avenue, as described in Assignment 1.

Karel should finish on the last avenue at 1st Street, facing east.
"""

from karel.stanfordkarel import *

def turn_right():# Let Karel turn left
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def repair_pillar():#repair a pillar an go back origin
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()
    turn_around()
    while  front_is_clear():
        move()
    turn_left()

def main():
    while front_is_clear():
        repair_pillar()
        for i in range(4):
            move()
    repair_pillar()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
