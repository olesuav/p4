from turtle import width
import pygame  # pygame-module needs to be imported
import sys     # sys-module will be needed to exit the game
from pygame.locals import * # pygame.locals gives us the constants of pygame
pygame.init()  # initializing pygame is mandatory in the beginning



width = 800 # leveys variable contains the width of the display-surface
height = 600 # korkeus variable contains the height of the display-surface
display = pygame.display.set_mode((width, height))
# the basic display-surface is created with set_mode(width,height) function
# pinta variable contains the display-surface, which is a Surface-object
pygame.display.set_caption("GOTY 2022")
# the caption of the display-window is set with set_caption() function



level = pygame.image.load("level.png").convert()
character = pygame.image.load("character.png").convert()
# pygame.image.load(file) function loads a picture file into a given variable
# convert() method converts the picture into the right pixel-format
# picture file needs to be in the same folder as this python file
# you can also specify the folder path, relatively or absolutely:
border_U = pygame.Surface((800,50))
border_D = pygame.Surface((800,50))
border_L = pygame.Surface((50,600)) #border for the top and bottom of the screen
border_R = pygame.Surface((50,600)) #border for the left and right of the screen
# Surface((x,y)) function creates empty black rectangle, x=width y=height
# level, hahmo, pallo and border are also Surface-objects, just like the display-surface



# the game also needs some RGB-colors (r,g,b), where 0<r,g,b<255
musta = (0,0,0)   # black color
puna = (255,0,0)  # red color
vihr = (0,255,0)  # green color
sini = (0,0,255)  # blue color
# Surface-objects can be filled with a color using fill() method
border_L.fill(musta)
border_D.fill(musta)
border_R.fill(musta)
border_U.fill(musta)

# Surface-objects can be added to the display-surface with blit() method
# blit(Surface,(x,y)) adds the Surface into coordinates (x,y)=(left, top)
display.blit(level, (0,0))
display.blit(border_L, (0,200))
display.blit(border_D, (0,200))
display.blit(border_R, (0,200))
display.blit(border_U, (0,200))

pygame.display.flip()
# the display-surface needs to be updated for the blitted Surfaces to become visible
# pygame.display.update() would do the same



# Rect-object holds the coordinates of a Surface-object
# Rect-objects are needed to move Surfaces and collision detection
# Surface.get_rect() method returns the Rect-object of the Surface
border_L_cord = border_L.get_rect()
border_R_cord = border_R.get_rect()
border_U_cord = border_U.get_rect()
border_D_cord = border_D.get_rect()
character_cord = character.get_rect()
# for example hahmoAlue = Rect(left,top,width,height) = (0,0,70,91)
# get_rect() method sets the left-top-corner to (0,0) by default
# hahmo and border were not blitted into (0,0)
# so we need to change the coordinates (left,right,top,bottom) with dot-notation
border_L_cord.left = 0
border_L_cord.top = 0
border_U_cord.left = 0
border_U_cord.top = 0
border_R_cord.left = 750
border_R_cord.top = 0
border_D_cord.left = 0
border_D_cord.top = 550
character_cord.left = 400
character_cord.top = 400


# endless game-loop which runs until sys.exit() and/or pygame.quit()
while True:

    
    # check if the user has closed the display-window or pressed esc
    for tapahtuma in pygame.event.get():  # all the events in the event queue
        if tapahtuma.type == pygame.QUIT: # if the player closed the window
            pygame.quit() # the display-window closes
            sys.exit()    # the whole python program exits
        if tapahtuma.type == KEYDOWN:     # if the player pressed down any key
            if tapahtuma.key == K_ESCAPE: # if the key was esc
                pygame.quit() # the display-window closes
                sys.exit()    # the whole python program exits





    # you can move hahmo-Surface with left,right,up,down-keys
    press = pygame.key.get_pressed()
    if press[K_UP]:
        character_cord.move_ip((0,-1))
    if press[K_DOWN]:
        character_cord.move_ip((0,1))
    if press[K_LEFT]:
        character_cord.move_ip((-1,0))
    if press[K_RIGHT]:
        character_cord.move_ip((1,0))
    # get.pressed() function gives a list of all the keys that are being pressed
    # from pygame-documentation you can find all the names for the keys

    #collision with the borders
    xd = [0,0]
    character_cord.move_ip(xd)

    if character_cord.colliderect(border_L_cord):
        character_cord[1] = -character_cord[1]
    #else:
    #    xd[0] = -xd[0]

    # draw all the Surfaces in their new places
    display.blit(level, (0,0)) # without this, moving characters would have a "trace"
    display.blit(border_L, border_L_cord)
    display.blit(border_D, border_D_cord)
    display.blit(border_R, border_R_cord)
    display.blit(border_U, border_U_cord)
    display.blit(character, character_cord)


    # this is always needed to the end to update the display surface
    pygame.display.flip()

