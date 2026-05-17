from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""


def main():
    move()
    spread_beepers()
    return_to_base()
    
def step_back():
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    move()

def spread_beepers():
    while beepers_present():
        pick_beeper()
        if beepers_present():
            while beepers_present():
                move()
            put_beeper()
            step_back()

def return_to_base():
    put_beeper()
    turn_around()
    move()
    turn_around()    

def turn_around():
    for i in range (2):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()