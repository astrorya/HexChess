import pygame
import numpy as np

pygame.init()
window_size_x = 1280
window_size_y = 896
screen = pygame.display.set_mode((window_size_x, window_size_y))
clock = pygame.time.Clock()
running = True
dt = 0

# Make a function to retrieve the pixel size of the board's image file, for now just manual
background = pygame.image.load('boards/hex-6x6x6.png').convert()
board_x = 808
board_y = 896

# pieces load
white_queen = pygame.image.load('pieces/white-queen.png').convert()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # center the board stuff
    board_window_x_diff = window_size_x - board_x
    center_board_x = board_window_x_diff / 2
    screen.blit(background, (center_board_x,0))
    colors = [(255, 255, 255), (206,206,206), (153,153,153)]
    # drawing the hexagons into the game rather than just a PNG
    
    # function for finding 6 vertices from the center
    
    def vertices(center):
        """
        Input "center" as pixel coordinates: [x, y]
        """
        side_length = 40/np.sin(np.pi/3) # pixels
        v1 = (center[0]+(side_length), center[1])
        v2 = (center[0]+(40/np.tan(np.pi/3)), center[1]-(40))
        v3 = (center[0]-(40/np.tan(np.pi/3)), center[1]-(40))
        v4 = (center[0]-(side_length), center[1])
        v5 = (center[0]-(40/np.tan(np.pi/3)), center[1]+(40))
        v6 = (center[0]+(40/np.tan(np.pi/3)), center[1]+(40))
        return [v1, v2, v3, v4, v5, v6]
    
    # trying to make just one hexagon
    pygame.draw.polygon(screen, (153,153,153), vertices([501, 447]))
    # Adding the blits for each piece
    screen.blit(white_queen, (501,447))
    
    
    # making a function for moving pieces with mouse
    
    def move(self, left_down=False, left_up=True, right_down=False, right_up=True):
            
    
    
    
    
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

pygame.quit()