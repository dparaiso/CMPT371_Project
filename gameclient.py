import socket
import pygame

#Initialize Pygame and set up the window
pygame.init()
width, height = 800, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Deny and Conquer')

#Array to hold 8x8 grid in a 1d array.
#Array values are 0 if unclaimed
#1 if claimed by Player 1, 2 if claimed by Player 2, etc.
grid_size = 8
array_data = [0] * grid_size * grid_size

# Constants for timing
CLICK_TIME_THRESHOLD = 1000  #Time in milliseconds for capturing a cell.
CLICKED = 1

# Variables to track clicking
click_start_time = None
current_clicked_cell = None

"""
Arguments:
pos - Cursor position (x,y) relative to top left corner.
cell_size - Size of 1 cell, equal to (width or height)/grid_size. Whichever is smaller.
Purpose:
Finds array index of the cell that was just clicked.
Index = width * row + col, as we are using a 1d array.
Returns:
Array index corresponding to the cell that was clicked.
"""
def get_cell_index(pos, cell_size):
    x, y = pos
    row_index = y // cell_size
    col_index = x // cell_size
    return row_index * grid_size + col_index
"""
Arguments:
pos - Cursor position (x,y) relative to top left corner.
Purpose:
Checks if the click was on a valid cell, and tracks how long it has been on the cell for.
"""
def handle_click(pos):
    global click_start_time, current_clicked_cell

    
    cell_size = min(width, height) // grid_size
    cell_index = get_cell_index(pos, cell_size)

    
    if 0 <= cell_index < len(array_data):
        if current_clicked_cell == cell_index:
            # Calculate time since the click started
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - click_start_time

            if elapsed_time >= CLICK_TIME_THRESHOLD:
                # Change the value of the clicked cell from 0 (unclicked) to 1 (clicked).
                array_data[cell_index] = CLICKED
                current_clicked_cell = None
                click_start_time = None

        else:
            # Start a new click event if the left mouse button is used.
            if pygame.mouse.get_pressed()[0] == 1:
                current_clicked_cell = cell_index
                click_start_time = pygame.time.get_ticks()
            else:
                current_clicked_cell = None
                click_start_time = None

def draw_array(array):
    #Start with a white canvas
    window.fill((255, 255, 255))  

    
    cell_size = min(width, height) // grid_size
    
    #Iterate through each element of the array and update the visuals accordingly.
    for index, item in enumerate(array):
        row_index = index // grid_size
        col_index = index % grid_size

        x = col_index * cell_size
        y = row_index * cell_size

        if item == CLICKED:
            # Cell is filled with sky blue if the value is 1 (clicked)
            # x+2, y+2 and cell_size - 4 are used to create a gap between each cell. Makes a more defined border for each cell.
            pygame.draw.rect(window, (135, 206, 235), (x + 2, y + 2, cell_size - 4, cell_size - 4))
        elif current_clicked_cell == index:
            # If the cell is currently being clicked, change the color based on the elapsed time
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - click_start_time
            progress = min(1, elapsed_time / CLICK_TIME_THRESHOLD)  # Calculate progress (0 to 1)

            # Interpolate between white and blue based on the progress
            # Progress is multiplied by a constant to get to the desired colour.
            r = int(255 * (1 - progress*0.470588235))
            g = int(255 * (1 - progress*0.19215686))
            b = 255
            pygame.draw.rect(window, (r, g, b), (x + 2, y + 2, cell_size - 4, cell_size - 4))
        else:
            # Cell is white if the value is 0 (not clicked and not being clicked)
            pygame.draw.rect(window, (255, 255, 255), (x + 2, y + 2, cell_size - 4, cell_size - 4))

        # Draw the borders for each cell
        pygame.draw.rect(window, (0, 0, 0), (x, y, cell_size, cell_size), 2)  # Border width = 2

        # Draws the status of the cell as text, in the middle of the cell.
        # Can be removed later, or changed to progress perhaps.
        font = pygame.font.Font(None, 24)
        text = font.render(str(item), True, (0, 0, 0))  
        text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
        window.blit(text, text_rect)

    # Draw vertical and horizontal lines to create grid borders
    # line(window, colour, start point, end point)
    for i in range(grid_size + 1):
        pygame.draw.line(window, (0, 0, 0), (i * cell_size, 0), (i * cell_size, height), 2)
        pygame.draw.line(window, (0, 0, 0), (0, i * cell_size), (width, i * cell_size), 2)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Get the current position of the mouse
        pos = pygame.mouse.get_pos()
        handle_click(pos)

        # Updates visuals based on clicks.
        draw_array(array_data)
        pygame.display.update()

#Main only gets run if this file is run directly.      
if __name__ == "__main__":
    main()
