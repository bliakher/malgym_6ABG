# import the pygame module, so you can use it
import pygame

width = 40

def draw_circle(surface, color, x, y):
  pygame.draw.circle(surface, color, (x, y), width // 2)
 
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
    # define a variable to control the main loop
    running = True

    x = width // 2
    y = screen_height // 2

    pressed = False
     
    # main loop
    while running:
        screen.fill((255, 255, 255))
        if x + width // 2 >= screen_width:
          draw_circle(screen,(0, 255, 0), x, y)
          pygame.display.update()
          continue

        screen.fill((255, 255, 255))
        draw_circle(screen,(255, 0, 0), x, y)

        pygame.display.update()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                  pressed = False
            if event.type == pygame.KEYDOWN:
        # check for specific key
                if event.key == pygame.K_RIGHT:
                  pressed = True

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        if pressed:
          x += 0.1

main()
