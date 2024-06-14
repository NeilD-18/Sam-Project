##
## Author: Kristina Striegnitz
##
## Version: Fall 2012
##
## If the player presses a keyboard key, the key's id and name gets
## printed to the screen.
##

import pygame
import random

def run_game():
    
    ## Initialize the pygame submodules and set up the display window.
    pygame.init()

    width = 640
    height = 480
    my_win = pygame.display.set_mode((width,height))
    mx = 0
    my = 0

    ## The game loop starts here.
    keepGoing = True    
    while (keepGoing):

        ## Handle events.
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                print("Key id: ", event.key)
                print("Key name: ", pygame.key.name(event.key))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                print("mouse clicked at pos: ",(mx,my))

        ## Draw picture and update display
        my_win.fill(pygame.color.Color("black"))
            
        pygame.display.update()

    ## The game loop ends here.

    pygame.quit()


## Call the function run_game.

run_game()
