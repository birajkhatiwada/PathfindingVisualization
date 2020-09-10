import pygame
import math
from Queue import PriorityQueue

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,255,0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))

pygame.display.set_caption("Path Finding Visualization")

def draw_grid(win, rows, width):
    boxSize = width // rows

    for x in range(rows):
        # line(surface, color, start_pos, end_pos, width) -> Rect
        pygame.draw.line(win, GREY, (0, x*boxSize), (width, x*boxSize))
        for y in range(rows):
            pygame.draw.line(win, GREY, (y*boxSize, 0), (y*boxSize, width))



running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    WIN.fill(BLACK)
    draw_grid(WIN, 50, WIDTH)
    pygame.display.update()
