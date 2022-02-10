# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen_width = 400
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((200, 255, 200))
     
    ball = pygame.image.load("ball.png")
    ball = pygame.transform.scale(ball, (50, 50))
    # define the position of the image
    xpos = 0
    ypos = 50
    # how many pixels we move our image each frame
    step_x = 1
    step_y = 1
    
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        if xpos>screen_width-50 or xpos<0:
            step_x = -step_x
        if ypos>screen_height-50 or ypos<0:
            step_y = -step_y
        # update the position of the smiley
        xpos += step_x # move it to the right
        ypos += step_y # move it down

        screen.fill((200, 255, 200))
        screen.blit(ball, (xpos, ypos))
        pygame.display.update()
        xpos += step_x
        

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

main()
