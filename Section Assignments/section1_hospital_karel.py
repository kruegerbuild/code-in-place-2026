from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():
    # because the spacings are not the same, we can use while loop and if function
    while front_is_clear():
        move()
        if beepers_present():
            build_hospital()

# write function to make hospital with 3x2 size
# 
def build_hospital():
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    for i in range(2):
        turn_right()
        move()
        put_beeper()
    move()
    put_beeper()
    turn_left()

# write function to turn right
def turn_right():
    for i in range(3):
        turn_left()

# omg I did it

if __name__ == '__main__':
    main()