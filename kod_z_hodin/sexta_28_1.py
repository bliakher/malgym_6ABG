# import the pygame module, so you can use it
import pygame

def draw_ball(surface, position):
  pygame.draw.circle(surface, (255, 0, 0), position, 5)
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen_width = 400
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
     
    # define a variable to control the main loop
    running = True

    x = screen_width // 2
    y = screen_height // 2
    speed = 0.05
    target_x = -1
    target_y = -1
    delta = 0.1

    moving = False
     
    # main loop
    while running:
        screen.fill((255, 255, 255))
        draw_ball(screen, (x, y))
        pygame.display.update()

        if moving:
            if (x < target_x + delta and x > target_x - delta) and ( y < target_y + delta and y > target_y - delta):
                moving = False
            else:
                dx = abs(target_x - x)
                dir_x = (target_x - x) // abs(target_x - x) if (target_x - x) != 0 else 0
                dy = abs(target_y - y)
                dir_y = (target_y - y) // abs(target_y - y) if (target_y - y) != 0 else 0
                distance = dx + dy
                sections = speed / distance
                move_x = dx * sections * dir_x
                move_y = dy * sections * dir_y
                x += move_x
                y += move_y
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                target_x = event.pos[0]
                target_y = event.pos[1]
                moving = True
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

main()
