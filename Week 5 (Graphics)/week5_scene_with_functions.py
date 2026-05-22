from graphics import Canvas
import math
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_sky(canvas, 'sky blue')
    draw_sun(canvas, 300, 210)
    draw_ground(canvas, 50, 'light green')
    draw_tree(canvas, 30, 200, 'dark green')
    draw_tree(canvas, 110, 185, 'green')
    draw_tree(canvas, 90, 300, 'dark red')
    draw_tree(canvas, 180, 210, 'salmon')
    draw_tree(canvas, 250, 240, 'orange')
    draw_cloud(canvas, 120, 10, 'beige')
    draw_cloud(canvas, -20, 50, 'light pink')
    draw_cloud(canvas, 320, 70, 'light grey')
    # TODO: draw two more clouds, and three trees

def draw_sun (canvas, x, y):
    canvas.create_oval(x, y, x + 130, y + 130, 'yellow')
def draw_sky(canvas, color):
    x1 = 0
    y1 = 0
    x2 = CANVAS_WIDTH
    y2 = CANVAS_HEIGHT

    canvas.create_rectangle(x1, y1, x2, y2, color)

def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in 
    different values of x and y (the location of the cloud) and
    color (the color of the cloud). 
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH
    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

def draw_tree(canvas, x, y, leaves_color):
    # Trunk
    half_trunk_x = TRUNK_WIDTH/2

    trunk_start_x = x - half_trunk_x
    trunk_end_x = x + half_trunk_x
    trunk_start_y = y - half_trunk_x
    trunk_end_y = y + TRUNK_HEIGHT

    canvas.create_rectangle(
        trunk_start_x,
        trunk_start_y,
        trunk_end_x,
        trunk_end_y,
        'saddlebrown')

    # leaves
    half_leaves = LEAVES_SIZE/2
    
    leaves_start_x = x - half_leaves
    leaves_end_x = x + half_leaves
    leaves_start_y = y - half_leaves
    leaves_end_y = y + half_leaves

    canvas.create_oval(
        leaves_start_x, 
        leaves_start_y,
        leaves_end_x,
        leaves_end_y,
        leaves_color)

def draw_ground(canvas, y, color):
    canvas.create_oval(-50 - CANVAS_WIDTH, CANVAS_HEIGHT - y, CANVAS_WIDTH + 50, CANVAS_HEIGHT + y, color)

if __name__ == '__main__':
    main()