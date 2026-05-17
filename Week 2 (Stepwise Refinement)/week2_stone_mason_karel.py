from karel.stanfordkarel import *

"""
File: main.py
--------------------
Karel has been hired to build the columns in the 
Temple of Artemis in Efes.

Karel starts at bottom left corner, 
facing right (aka east).

The columns are exactly four squares apart, 
on the 1st, 5th, 9th, and 13th columns.

Karel can assume that columns are always five units high.

When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    for i in range (3):
        build_column()
        for j in range (4): 
            move()
    build_column() #fencepost

def build_column():
    turn_left()
    for i in range (4):
        put_beeper()
        move()
    put_beeper() #fencepost
    turn_back()
    while front_is_clear():
        move()
    turn_left()

def turn_back():
    for i in range (2):
        turn_left()
    pass

if __name__ == '__main__':
    main()