from karel.stanfordkarel import *

"""
1. Karel put beeper at first and last column in the row
2. Karel go back and forth. If there is a beeper, then move
3. Karel fill out row
4. Karel goes to last column first and then take beeper, then Karel does it back and forth
"""

def main():
    fill_row()
    reset()
    while beepers_present():
        remove_from_sides()
    if facing_east():
        turn_around()
        move()
        turn_around()
    else:
        turn_around()
    put_beeper()
        

def fill_row():
    while front_is_clear():
        put_beeper()
        move()  
    put_beeper()
    
def reset():
    if front_is_blocked():
            turn_around()
            move_to_wall()
            turn_around()

def remove_from_sides():
    pick_beeper()
    move()
    while beepers_present() and front_is_clear():
        move()
    turn_around()
    if no_beepers_present():
        move()

def turn_around():
    for i in range(2):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

if __name__ == '__main__':
    main()