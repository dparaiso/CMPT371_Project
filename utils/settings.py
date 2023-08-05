import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

FPS = 120

WIDTH, HEIGHT = 608, 608                        #size of display for 8x8 grid
                                                #608/8 = 76
ROWS = COLS = 152                               #number of row/cols in display
                                                #152/8 = 19 means 19x19 pixel grid box
                                              #361 is total pixel in grid box
                                                #361/2 = 181 pixel to fill more than half grid box
# TOOLBAR_HEIGHT = HEIGHT - WIDTH
Number_of_Player = 2 

PIXEL_SIZE = WIDTH // COLS                      #pixel size 4 

BG_COLOR = WHITE

DRAW_GRID_LINES = True

def init_grid(rows, cols, color):               #not needed?
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    
    return grid   

grid = init_grid(ROWS, COLS, BG_COLOR)



def get_font(size):
    return pygame.font.SysFont("comicsans", size)


 