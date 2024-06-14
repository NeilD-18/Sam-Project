##
## Authors: John Rieffel/Kristina Striegnitz
##
## Version: Fall 2014
##
## This program shows a blue sky with white clouds and a bat 
## sitting in the upper left hand corner. There is also some music
## playing.

import pygame


def run_game():

    ## Initialize the pygame submodules and set up the display window.

    pygame.init()

    # load background pic
    sky = pygame.image.load("sky_scaled.bmp")

    # create pygame window; make the window as big as the background
    # image
    width = sky.get_width()
    height = sky.get_height()
    my_win = pygame.display.set_mode((width,height))

    # prepare background pic
    sky = sky.convert()

    ## Load other resources
    pygame.mixer.music.load("mario_bros_trimmed.ogg")
    pygame.mixer.music.play(-1)

    bat = pygame.image.load("bat.bmp")
    bat = bat.convert()
    
    ## Initialize game objects


    ## The game loop starts here.
    
    keepGoing = True    
    while (keepGoing):

        ## Handle events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            #elif event.type == pygame.MOUSEBUTTONUP:
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                print("hello", mx,my)


        ## Simulate game world

 

        ## Draw picture and update display

        my_win.blit(sky, (0,0))

        my_win.blit(bat, (0,0))

        pygame.display.update()

    ## The game loop ends here.

    pygame.quit()


## Call the function run_game.

run_game()
