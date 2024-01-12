import pygame
import numpy

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
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

pygame.quit()