`main.py`
```python

import pygame

black = pygame.Color(0,0,0)
yellow = pygame.Color(255, 255, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(101, 67, 33)
dark_brown = pygame.Color(56, 37, 14)
red = pygame.Color(255, 0, 0)
beige = pygame.Color(244, 226, 198)
blue = pygame.Color(0, 0, 255)
light_blue = pygame.Color(200, 200, 255)
grey = pygame.Color(220, 220, 220)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Square:
    def __init__(self, size, position, color):
        self.size = size
        self.color = color
        self.position = position

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, 
            pygame.Rect(self.position.x, self.position.y, self.size, self.size))
        
class Wall:
    def __init__(self, position, width):
        self.square = Square(width, position, brown)

    def draw(self, surface):
        self.square.draw(surface)

class Floor:
    def __init__(self, position, width):
        self.square = Square(width, position, beige)

    def draw(self, surface):
        self.square.draw(surface)

class Map:
    def __init__(self, tile_width, corner):
        self.map = []
        self.tile_width = tile_width
        self.corner = corner

    def load_from_file(self, file_name):
        with open(file_name) as f:
            j = 0
            for line in f.readlines():
                row = []
                i = 0
                for c in line.strip():
                    position = Point(self.corner.x + i * self.tile_width, self.corner.y + j * self.tile_width)
                    if c == 'X':
                        wall = Wall(position, self.tile_width)
                        row.append(wall)
                    if c == ' ':
                        floor = Floor(position, self.tile_width)
                        row.append(floor)
                    i += 1
                self.map.append(row)
                j += 1

    def draw(self, surface):
        for i in range(len(self.map[0])):
            for j in range(len(self.map)):
                tile = self.map[j][i]
                tile.draw(surface)

 
# define a main function
def main():
     
    pygame.init()
    pygame.display.set_caption("minimal program")
     
    screen_width = 400
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))

    screen.fill((255, 255, 255))
    
    map = Map(10, Point(0, 0))
    map.load_from_file("map.txt")
    map.draw(screen)
    pygame.display.update()

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
```

`map.txt`
```
XXXXXXXXXX
X    X   X
XXXX X   X
X X  XX XX
X XX X   X
X  X XXX X
XX   X   X
XXXX   XXX
X X  X   X
XXXXXXXXXX
```
