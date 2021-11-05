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
    screen = pygame.display.set_mode((400,300))
    screen.fill((200, 255, 200))
     
    cat = pygame.image.load("cat.png")
    screen.blit(cat, (100,50))

    ball = pygame.image.load("ball.png")
    ball = pygame.transform.scale(ball, (50, 50))
    screen.blit(ball, (110, 210))
    
    pygame.display.update()

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

main()
