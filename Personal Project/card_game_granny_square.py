from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
PATTERN_SIZE = 100

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # draw the first row
    draw_heart_pattern(canvas, 0, 0)
    draw_diamond_pattern(canvas, PATTERN_SIZE, 0)
    draw_heart_pattern(canvas, PATTERN_SIZE*2, 0)
    draw_diamond_pattern(canvas, PATTERN_SIZE*3, 0)
    # draw the second row
    draw_spade_pattern(canvas, 0, PATTERN_SIZE)
    draw_club_pattern(canvas, PATTERN_SIZE, PATTERN_SIZE)
    draw_spade_pattern(canvas, PATTERN_SIZE*2, PATTERN_SIZE)
    draw_club_pattern(canvas, PATTERN_SIZE*3, PATTERN_SIZE)
    # draw the third row
    draw_heart_pattern(canvas, 0, PATTERN_SIZE*2)
    draw_diamond_pattern(canvas, PATTERN_SIZE, PATTERN_SIZE*2)
    draw_heart_pattern(canvas, PATTERN_SIZE*2, PATTERN_SIZE*2)
    draw_diamond_pattern(canvas, PATTERN_SIZE*3, PATTERN_SIZE*2)
    # draw the fourth row
    draw_spade_pattern(canvas, 0, PATTERN_SIZE*3)
    draw_club_pattern(canvas, PATTERN_SIZE, PATTERN_SIZE*3)
    draw_spade_pattern(canvas, PATTERN_SIZE*2, PATTERN_SIZE*3)
    draw_club_pattern(canvas, PATTERN_SIZE*3, PATTERN_SIZE*3)

def draw_heart_pattern(canvas, start_x, start_y):
    # draw pattern at (start_x, start_y)
    end_x = start_x + PATTERN_SIZE
    end_y = start_y + PATTERN_SIZE
    # draw beige square background
    canvas.create_rectangle(start_x, start_y, end_x, end_y, 'beige')
    # draw heart shape
    half_x = PATTERN_SIZE/2
    half_y = PATTERN_SIZE/2
    inset = 20
    canvas.create_oval(start_x+inset, start_y+inset, start_x+half_x+1, start_y+half_y+1, 'maroon')
    canvas.create_oval(start_x+half_x-1, start_y+inset, end_x-inset, start_y+half_y+1, 'maroon')
    canvas.create_polygon(start_x+inset, start_y+half_y-10, end_x-inset, start_y+half_y-10, start_x+half_x, end_y-inset, color='maroon')

def draw_diamond_pattern(canvas, start_x, start_y):
    # draw pattern at (start_x, start_y)
    end_x = start_x + PATTERN_SIZE
    end_y = start_y + PATTERN_SIZE
    # draw maroon square background
    canvas.create_rectangle(start_x, start_y, end_x, end_y, 'maroon')
    # draw diamond shape
    half_x = PATTERN_SIZE/2
    half_y = PATTERN_SIZE/2
    inset = 20
    canvas.create_polygon(start_x+inset+5, start_y+half_y, end_x-inset-5, start_y+half_y, start_x+half_x, start_y+inset, color='beige')
    canvas.create_polygon(start_x+inset+5, start_y+half_y, end_x-inset-5, start_y+half_y, start_x+half_x, end_y-inset, color='beige')

def draw_spade_pattern(canvas, start_x, start_y):
     # draw pattern at (start_x, start_y)
    end_x = start_x + PATTERN_SIZE
    end_y = start_y + PATTERN_SIZE
    # draw dark blue square background
    canvas.create_rectangle(start_x, start_y, end_x, end_y, '#5B6D7A')
    # draw spade shape
    half_x = PATTERN_SIZE/2
    half_y = PATTERN_SIZE/2
    inset = 20   
    canvas.create_oval(start_x+inset, start_y+half_x, start_x+half_x+1, end_y-inset-5, 'beige')
    canvas.create_oval(start_x+half_x-1, start_y+half_x, end_x-inset, end_y-inset-5, 'beige')
    canvas.create_polygon(start_x+inset, end_y-inset-21, end_x-inset, end_y-inset-21, start_x+half_x, start_y+inset, color='beige')
    canvas.create_polygon(start_x+half_x-10, end_y-inset+5, end_x-half_x+10, end_y-inset+5, start_x+half_x, end_y-half_y+17, color='beige')

def draw_club_pattern(canvas, start_x, start_y):
     # draw pattern at (start_x, start_y)
    end_x = start_x + PATTERN_SIZE
    end_y = start_y + PATTERN_SIZE
    # draw beige square background
    canvas.create_rectangle(start_x, start_y, end_x, end_y, 'beige')
    # draw club shape
    half_x = PATTERN_SIZE/2
    half_y = PATTERN_SIZE/2
    inset = 20 
    canvas.create_oval(start_x+inset, start_y+half_y-5, end_x-half_x, end_y-inset-5, '#5B6D7A')
    canvas.create_oval(start_x+half_x, start_y+half_y-5, end_x-inset, end_y-inset-5, '#5B6D7A')
    canvas.create_oval(start_x+inset+15, start_y+inset, end_x-half_x+15, end_y-half_y, '#5B6D7A')    
    canvas.create_polygon(start_x+half_x-10, end_y-inset+5, end_x-half_x+10, end_y-inset+5, start_x+half_x, end_y-half_y+11, color='#5B6D7A')
    # fill the middle of the shape
    canvas.create_polygon(start_x+half_x-10, end_y-half_y-5, end_x-half_x+10, end_y-half_y-5, start_x+half_x, end_y-half_y+10, color='#5B6D7A')


if __name__ == '__main__':
    main()