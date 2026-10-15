"""
File: CollectNewspaperKarel.py
Name: Andrew
--------------------------------
At the start, this program does nothing.

Your task is to add the necessary code
to guide Karel to walk to the door of its house,
pick up the newspaper (represented by a beeper),
and then return to its original position
in the upper-left corner of the house.
"""

from karel.stanfordkarel import *
def turn_right():# Let Karel turn left
    for i in range(3):
        turn_left()

def turn_around():#Let Karel turn around
    for i in range(2):
        turn_left()
def take_news_paper():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()

def back_home():
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()



def main():
    """
    Pre_condition: In the home.
    Post_condition:In the home
    """
    take_news_paper()
    back_home()




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
