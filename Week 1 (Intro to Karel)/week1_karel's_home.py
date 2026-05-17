from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    karel_go_out()
    pick_beeper()
    turn_around() #Karel facing west to go home
    karel_go_home()
    
#pre-condition: Karel facing east and stands in the corner
#post_condition: Karel facing east and stands on the beeper
def karel_go_out():
    for i in range(2):
            move()
        turn_right()
        move()
        turn_left()
        move()

#pre-condition: Karel facing west and standing outside of her house
#post-condition: Karel facing east standing at the corner again
def karel_go_home():
    move()
    turn_right()
    move()
    turn_left()
    for i in range (2):
        move()
    turn_around()


def turn_around():
    for i in range (2):
        turn_left()

def turn_right():
    for i in range (3):
        turn_left()
    
    
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()