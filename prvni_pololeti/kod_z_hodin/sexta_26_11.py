# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen_width = 400
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))

    screen.fill((255, 255, 255))

    black = pygame.Color(0,0,0)
    yellow = pygame.Color(255, 255, 0)
    white = pygame.Color(255, 255, 255)

    pygame.draw.circle(screen, yellow, (100, 100), 50)
    pygame.draw.circle(screen, white, (120, 105), 45)

    pygame.draw.circle(screen, yellow, (300, 200), 50, width=10)
    

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
