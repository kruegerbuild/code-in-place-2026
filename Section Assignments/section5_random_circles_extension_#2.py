from graphics import Canvas
import random

'''
Draw circles of a random size 
'''

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = random.randint(10, 40)
N_CIRCLES = 20

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range (N_CIRCLES):
        draw_random_circles(canvas)

def draw_random_circles(canvas):
    random_x = random.randint(0, CANVAS_WIDTH)
    random_y = random.randint(0, CANVAS_HEIGHT)
    canvas.create_oval(
        random_x, 
        random_y, 
        random_x + CIRCLE_SIZE, 
        random_y + CIRCLE_SIZE, 
        random_color()
        )
    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

'''
Note for myself:
At first I just use random_coordinate(0,300).
Turns out the circles were stacking into a linear shape (negative correlation pattern)
So instead i made 2 different variables, 1 for x coordinate,
1 for y coordinate. And boom!
'''

if __name__ == '__main__':
    main()