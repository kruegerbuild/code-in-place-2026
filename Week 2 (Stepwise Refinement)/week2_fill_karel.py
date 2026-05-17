from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers
regardless of its size. 

Decomposition:
1. Karel fills a row with beepers (note that 
there is are walls beside Karel
on each row).
2. Karel return to the first column.
3. Karel will ascend a row.
4. Repeat until Karel reaches the last column on last row.
"""

def main():
    while left_is_clear():
        fill_row()
        return_to_first_column()
        ascend_one_row()
    fill_row() #fencepost

def return_to_first_column():
    turn_around()
    move_to_wall()

def ascend_one_row():
    turn_right()
    move()
    turn_right()
        
def fill_row():
    while front_is_clear():
        put_beeper()
        move()
    if front_is_blocked():
        put_beeper()

#fundamental functions:

def turn_around():
    for i in range (2):
        turn_left()

def turn_right():
    for i in range (3):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()