import pygame
import math
from Queue import PriorityQueue
from node import Node


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

WIDTH = 600
ROWS = 40
GAP = WIDTH // ROWS

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Visualization")


def make_grid():
    grid = []
    for x in range(ROWS):
        grid.append([])
        for y in range(ROWS):
            nod = Node(x, y)
            grid[x].append(nod)

    return grid


def draw_grid():
    for x in range(ROWS):
        # line(surface, color, start_pos, end_pos, width) -> Rect
        pygame.draw.line(WIN, GREY, (0, x*GAP), (WIDTH, x*GAP))
        for y in range(ROWS):
            pygame.draw.line(WIN, GREY, (y*GAP, 0), (y*GAP, WIDTH))


def get_clickedPos(pos):
    x, y = pos
    col = x // GAP
    row = y // GAP
    return row, col


def main():
    start = None
    end = None

    grid = make_grid()
    WIN.fill(WHITE)
    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False

        draw_grid()
        pygame.display.update()
        if pygame.mouse.get_pressed()[0]: #Left
            pos = pygame.mouse.get_pos()
            col, row = get_clickedPos(pos)
            print(row, col)
            spot = grid[row][col]
            if not start and spot != end:
                start = spot
                spot.make_startNode()

            elif not end and spot != start:
                end = spot
                spot.make_endNode()

            elif spot != start and spot != end and not spot.is_barrierNode():
                spot.make_barrierNode()

            spot.drawNode(WIN)
            pygame.display.update()



main()