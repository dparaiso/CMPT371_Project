import pygame
from utils import *
class player():                                         #Player object to track player data
    def __init__(self, pos, color, active_box, pixel_count):
        self.pos = pos                                  #current player pos for active grid/ pixel colour
        self.color = color                              #current player colour
        self.active_box = active_box                    #current player active box number from grid
        self.occupied_Count = 0                         #current player occupied box count 
        self.occupied_boxes = []                        #current player list of occupied box
        self.pixel_count = pixel_count                  #current player coloured pixel count for active box
        self.common_occupied_boxs = []                  #All player list of occupied box
        self.cursor = (304,304)                              #Current player cursor postion initialization
        self.otherActive_box = []
        self.Failed_to_occupy = []
        self.status = -1
     
        
    def Play(self):
        # print("In Play function : ")
        # print( "active box : ", self.active_box)
        # print ("occupied box: ", self.occupied_Count)
        # print ("count ", self.pixel_count)
        # print ("occupied box", self.occupied_boxes)
        #self.cursor = pygame.mouse.get_pos()
        self.Failed_to_occupy = [] 
        if pygame.mouse.get_pressed()[0]:                               #no need to check?
            pos = pygame.mouse.get_pos()                                #getting pos if mouse is pressed
        else:
            return
                                    #checking if pos is in active boxs of other player in game
        if get_grid_box_number(pos) in self.otherActive_box:
                                                        #if yes then return
            return
        for k in self.common_occupied_boxs: 
                                           #checking if pos is in occupied boxs in game
                if get_grid_box_number(pos) in k[0]:                    #if yes then return
                    self.active_box = None
                    return
        row, col = get_row_col_from_pos(pos)                            #getting row,col from pos as per pixel
        if self.active_box == None:                                     #setting active grid for the first click
            grid[row][col] = self.color                      #not needed? updating colour and required pos variable to track 
            self.pixel_count = self.pixel_count+1
            self.active_box = get_grid_box_number(pos)
            self.pos = pos
            
        if self.active_box != None:                             
            if  get_grid_box_number(pos) == self.active_box:            #checking for pos inside active box
                if grid[row][col] == BG_COLOR:                          #updating pixel count and colouring box
                    grid[row][col] = self.color                         #not needed?
                    self.pixel_count = self.pixel_count+1
                    self.pos = pos
                    # print(self.pixel_count)
            else: return    
                
        
            if self.pixel_count >= 181:                                 #current player coloured more thean half of pixel
                                                                        #updated active box to occuped box
                self.occupied_boxes.append(get_grid_box_number(self.pos))
                # self.common_occupied_boxs.append([self.active_box,self.color])
                self.occupied_Count += 1
                self.active_box = None
                self.pixel_count = 0

                pygame.display.update()
        
        return         
    def Reset(self):
        if self.active_box != None: 
            self.Failed_to_occupy.append(self.active_box)
            self.active_box = None
            self.pixel_count = 0

    def get_occupied_boxes(self):                                       #return current occupied boxes
        return self.occupied_boxes
    
    def set_common_box(self, comm):                                     #set common occupied boxes of all
        self.common_occupied_boxs = comm

    def get_pos(self):                                                  #get/set pos for cursor
        return self.cursor   
    def set_pos(self, pos):
        self.cursor = pos
    def get_Active_box(self):
        return self.active_box
    def set_other_active_box(self, boxes):
        self.otherActive_box = boxes
    def get_failed_to_occupy(self):
        return self.Failed_to_occupy
    def Reset_failed_to_occupy(self):
        self.Failed_to_occupy = []  
    def set_failed_to_occupy(self, Value):
        self.Failed_to_occupy = Value
    def get_status(self):
        return self.status
    def set_status(self, num):
        self.status = num         






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