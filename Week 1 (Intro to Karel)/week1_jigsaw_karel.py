from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""

def main():
   karel_pick_beeper()
   karel_goes_to_puzzle()
   put_beeper()
   turn_around()
   karel_go_home()

def karel_go_home():
    for i in range (2):
        move()
    turn_right()
    for i in range (3):
        move()
    for i in range (2):
        turn_left()

def turn_around():
    for i in range (2):
        turn_left()

def karel_pick_beeper():
    for i in range(2):
        move()
    pick_beeper()

def karel_goes_to_puzzle():
    move()
    turn_left()
    for i in range (2):
        move()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()