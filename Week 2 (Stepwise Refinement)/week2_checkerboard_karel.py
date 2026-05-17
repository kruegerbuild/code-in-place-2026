from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers in checkerboard pattern.
"""


def main():
    put_beeper()
    while left_is_clear():
        checker_row()
        ascend_row_and_setup()
    checker_row()
    go_back()

def go_back():
    turn_right()
    move_to_wall()
    turn_left()

def ascend_row_and_setup():
    if beepers_present():
        ascend_row()
    else:
        ascend_row()
        put_beeper() #without this function the world won't be in checkerboard pattern

def ascend_row():
    turn_left()
    move()
    turn_right()

def checker_row():
    if beepers_present():
        if front_is_clear(): #because the program should be able to operate in any world
            move()
            checker_from_empty_corner()
    else:
        checker_from_empty_corner()
    return_to_first_column()

def return_to_first_column():
    turn_back()
    move_to_wall()
    turn_back()    

def checker_from_empty_corner():
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear(): #needed because while loop will begin if the first condition is true, thus there will be an error.
            move()


# basic function

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range (3):
        turn_left()

def turn_back():
    for i in range (2):
        turn_left()

    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()