from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(N_BOXES):
        left_x= i*BOX_SIZE
        top_y= 120
        right_x= left_x+BOX_SIZE
        bottom_y= top_y+BOX_SIZE
        rect = canvas.create_rectangle(left_x,top_y,right_x,bottom_y,"White","Black")
    

if __name__ == '__main__':
    main()
    