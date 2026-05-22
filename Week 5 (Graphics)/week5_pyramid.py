from graphics import Canvas
import random
import time

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for r in range (BRICKS_IN_BASE):
        bricks_in_row = BRICKS_IN_BASE - r
        row_width = bricks_in_row * BRICK_WIDTH
        start_x = (CANVAS_WIDTH - row_width) / 2
        for c in range (bricks_in_row):
            left_x = start_x + c * BRICK_WIDTH
            right_x = left_x + BRICK_WIDTH

            top_y = CANVAS_HEIGHT - (r + 1) * BRICK_HEIGHT
            bottom_y = top_y + BRICK_HEIGHT

            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'orange', 'black')

            time.sleep(0.05)
        
'''
rows: for r in range (BRICKS_IN_BASE)
column: for c in range (BRICKS_IN_BASE)
'''

if __name__ == '__main__':
    main()