import pygame
import random

pygame.init()

#screen size
display_width = 800
display_height = 600

#game display
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('dodge')

#set colours
black = (0,255,255)
white = (0,0,0)

#size of ball(for collision)
ball_width = 24

#score counter
dodged = 0

clock = pygame.time.Clock()

#game state
crashed = False

#importing ball image
ballImg = pygame.image.load('ball.png')
ballImg = pygame.transform.scale(ballImg, (30, 24))

#importing asteroid
asteroid = pygame.image.load('asteroid-modified.png')
asteroid = pygame.transform.scale(asteroid, (100, 100))


#displays score counter in top left
def objects_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

#states and draws objects(obstacles falling from screen)
def objects(object_x, object_y, object_w, object_h, color):
    asteroid = pygame.image.load('asteroid-modified.png')
    gameDisplay.blit(asteroid, (object_x,object_y))
    #pygame.draw.rect(gameDisplay, color, [object_x, object_y, object_w, object_h])

#shows image on screen with coordinates
def ball(x,y):
    gameDisplay.blit(ballImg, (x,y))


x =  (display_width * 0.45)
y = (display_height * 0.8)

#variables for movement
x_change = 0
y_change = 0

#characteristics of falling objects
object_startx = random.randrange(0,display_width)
object_starty = -600
object_speed = 7
object_width = 125
object_height = 125

#start game loop
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            pygame.quit()
            quit()
        #ball movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -5
            elif event.key == pygame.K_d:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    #movement
    x += x_change
    y += y_change

    #background display
    gameDisplay.fill(white)

    #restates variables and adds speed variable
    objects(object_startx, object_starty, object_width, object_height, black)
    object_starty += object_speed

    #shows ball    
    ball(x,y)

    #shows score counter
    objects_dodged(dodged)

    #adds boundaries for ball
    if x > display_width - ball_width or x < 0:
        crashed = True
        print("You can't escape")
        print("You dodged", dodged ,"objects")

    #keeps respawning block at top once gets past screen, increases score
    if object_starty > display_height:
        object_starty = 0 - object_height
        object_startx = random.randrange(0,display_width - object_width)
        dodged += 1

    #collison, if x and y coords align, game stops
    if y < object_starty+object_height:
            if x > object_startx and x < object_startx + object_width or x+ball_width > object_startx and x + ball_width < object_startx+object_width:
                crashed = True
                print("You dodged", dodged ,"objects")

    #difficulty settings
    if dodged == 3:
        object_speed = 10

    elif dodged == 7:
        object_speed = 15

    elif dodged == 15:
        object_speed = 20

    elif dodged == 22:
        object_speed = 25

    elif dodged == 30:
        object_speed = 30

    elif dodged == 37:
        object_speed = 35

    elif dodged == 42:
        object_speed = 40

    #updates screen    
    pygame.display.update()
    clock.tick(60)

#exit game
pygame.quit()
quit()
