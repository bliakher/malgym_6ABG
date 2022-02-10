# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen_width = 600
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))

    cat = pygame.image.load("cat.png")
    cat = pygame.transform.scale(cat, (100, 100))
    
    x = 0
    y = 50
    step = 1

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        screen.fill((255, 255, 255))

        screen.blit(cat, (x, y))

        x += step
        if x < 0 or x > screen_width - 100:
            step *= -1   

        pygame.display.update()


        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

main()
