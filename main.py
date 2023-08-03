from utils import *
from Player import player
from client import Network
import sys
import time

WIN = pygame.display.set_mode((WIDTH, HEIGHT))                          
pygame.display.set_caption("Game Name")


def init_grid(rows, cols, color):                               #setting grid
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    
    return grid



def draw_grid(win, grid):                                       # drawing grid
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i *
                                          PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS +1): #row +1
            pygame.draw.line(win, BLACK, (0, i * 76),
                             (WIDTH, i * 76))

        for i in range(COLS +1): # col +1 
            pygame.draw.line(win, BLACK, (i * 76, 0),
                             (i * 76, HEIGHT))


def draw(win, grid):                                            #draw grid on display
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    # for button in buttons:
    #     button.draw(win)

    pygame.display.update()

def col_grid(win,grid, Player1, Player2):                       #updating all display as per activity
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    x,y = get_row_col_from_pos(Player1.pos)                     #coloring pixel for player 1
    grid[x][y] = Player1.color
    i,j = get_row_col_from_pos(Player2.pos)                     #coloring pixel for player 2
    grid[i][j] = Player2.color

    if Player1.pixel_count < 2:
        grid[x][y] = BG_COLOR
    if Player2.pixel_count < 2:
        grid[i][j] = BG_COLOR    

    #surf1 = pygame.Surface((8,8))
    pygame.draw.circle(win, Player2.color, Player2.get_pos(), 8) #other player cursor as circle   
  

    surf = pygame.Surface((8,8))
    surf.fill((Player1.color))
    color = pygame.cursors.Cursor((6,6), surf)
    pygame.mouse.set_cursor(color)                               #current player square cursor

    
    pygame.display.update()                                      #updating display

    common_occupied = []                                         #new list for already occupied boxes
    
    if Player1.occupied_Count != 0:                              # adding occupied boxes to list
        common_occupied.append([Player1.get_occupied_boxes(), [Player1.color]])
       
    if Player2.occupied_Count != 0:    
        common_occupied.append([Player2.get_occupied_boxes(), [Player2.color]])
    if (common_occupied.count != 0):                             #updating common occupied box for player
        Player1.set_common_box(common_occupied)
        Player2.set_common_box(common_occupied)    
    
    #print (common_occupied)
    #print(Player1.common_occupied_boxs or Player2.common_occupied_boxs)
    for k in common_occupied:                                    #Box is filled with colour of occupied player
        for item in k[0]:    
            x,y = item
            # print (x,y)
            # print (k[1])
            x1 = (x-1)*76 // PIXEL_SIZE
            x2 = x*76 // PIXEL_SIZE
            y1 = (y-1)*76 // PIXEL_SIZE
            y2 = y*76 // PIXEL_SIZE
            X = range(x1,x2)
            Y = range(y1,y2)
            for i in X:
                for j in Y:
                    grid[i][j] = k[1][0]

    active_box = []
    active_box.append(Player2.get_Active_box())
    #active_box.append(Player2.get_Active_box())
    #Player1.set_other_active_box(active_box)
    # print(active_box)
    if active_box != None:
        Player1.set_other_active_box(active_box)
    
    failed_gird = []
    failed_gird.append(Player1.get_failed_to_occupy())
    failed_gird.append(Player2.get_failed_to_occupy())
    #print(failed_gird)
    #Player2.set_failed_to_occupy()
    for k in failed_gird:                                    #Box is filled with colour of occupied player
        for item in k:    
            x,y = item
            # print (x,y)
            # print (k[1])
            x1 = (x-1)*76 // PIXEL_SIZE
            x2 = x*76 // PIXEL_SIZE
            y1 = (y-1)*76 // PIXEL_SIZE
            y2 = y*76 // PIXEL_SIZE
            X = range(x1,x2)
            Y = range(y1,y2)
            for i in X:
                for j in Y:
                    grid[i][j] = BG_COLOR
    # Player1.Reset_failed_to_occupy()
    # Player2.Reset_failed_to_occupy()
    # 
    if Player1.occupied_Count >= 33:#(64 // Number_of_Player):
         Player1.set_status(1)
         Player2.set_status(0)
    if Player2.occupied_Count >= 33:#(64 // Number_of_Player):     
         Player1.set_status(0)
         Player2.set_status(1)

    if Player1.get_status() == 1:     
        message_to_screen("You Won", p.color)
        print ("you won")
        # raise IndexError
    if Player1.get_status() == 0:     
        message_to_screen("You Lose", p.color) 
        print ("you lose")
        # raise IndexError              
    
    
def message_to_screen (msg, color):
    WIN.fill(color)
    font = get_font(30)
    screen_text = font.render(msg, True, BG_COLOR)    
    WIN.blit(screen_text, [304,304]) 
    pygame.display.update()
    time.sleep(20)    
   
   
    


def get_row_col_from_pos(pos):                           # returning row,col positing as per pixel size (4)
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE
   
    if row >= ROWS:
        raise IndexError

    return row, col

def get_grid_box_number(pos):                           # returning box position from the grid.
    row, col = pos
    
    
    if (row >= 0 and row <=76):
        y=1
    if(row >76 and row <=152):
        y=2
    if(row >152 and row <=228):
        y=3
    if(row >228 and row <=304):
        y=4
    if(row >304 and row <=380):
        y=5
    if(row >380 and row <=456):
        y=6
    if(row >456 and row <=532):
        y=7
    if(row >532 and row <=608):
        y=8

    if (col >= 0 and col <=76):
        x=1
    if(col >76 and col <=152):
        x=2
    if(col >152 and col <=228):
        x=3
    if(col >228 and col <=304):
        x=4
    if(col >304 and col <=380):
        x=5
    if(col >380 and col <=456):
        x=6
    if(col >456 and col <=532):
        x=7
    if(col >532 and col <=608):
        x=8

    return x,y                      
    



                                                        #Initialization
run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = RED
pixel_count = 0
previous_pos = None
inactive_grid_box = []

#p = player((2,2),RED,None,grid,pixel_count)
n = Network()                                           #setting network
                                           #getting player object from connection
#print(p.pos, p.color)
if len(sys.argv) == 2:
  n.set_server(sys.argv[1])
p = n.getP() 

while run:
    clock.tick(FPS)
    
    p2 = n.send(p)                                      #sending and receving p,p2 object
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # try:
        p.set_pos(pygame.mouse.get_pos())               #getting/setting cursor position of current player
        if pygame.mouse.get_pressed()[0]:
        # p.pos = pygame.mouse.get_pos() 
        
            p.Play()                                    #calling Play() if mouse is pressed 
        else:    
            p.Reset() 
            
                    
    
                #     # p.pos = pos
                #     # p.Play()
                    
        # except IndexError:
            while p.get_status() == 1:
                message_to_screen("You Won", p.color)
                
            while p.get_status() == 0:
                message_to_screen("You Lose", p.color)
                
            #run = False
            #     continue
              
    draw(WIN, grid)
    col_grid(WIN, grid, p,p2)                            # Updating screen as per activity
     

pygame.quit()
