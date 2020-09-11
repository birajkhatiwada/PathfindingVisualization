import pygame
import math
from Queue import PriorityQueue
from node import Node

WHITE = (207, 224, 232)
GREY = (128, 128, 128)
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

def draw(grid):
    for row in grid:
        for node in row:
            node.drawNode(WIN)

    draw_grid()
    pygame.display.update()


def get_clickedPos(pos):
    x, y = pos
    col = x // GAP
    row = y // GAP
    return row, col

def construct_path(came_from, current, grid):
    while current in came_from:
        current = came_from[current]
        current.make_pathNode()
        draw(grid)


def algorithm(grid, start, end):
    visited = []
    unvisited = []
    came_from = {}
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    distance_from_start = {node: float("inf") for row in grid for node in row}
    distance_from_start[start] = 0
    open_set_hash = {start}

    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)
        if current == end:
            construct_path(came_from, end, grid)
            return True

        for neighbor in current.get_neighbors():
            temp_distance_from_start = distance_from_start[current] + 1
            if temp_distance_from_start < distance_from_start[neighbor]:
                came_from[neighbor] = current
                distance_from_start[neighbor] = temp_distance_from_start
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((distance_from_start[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_openNode()

        draw(grid)
        # pygame.display.update()
        if current != start:
            current.make_closedNode()


def main():
    start = None
    end = None

    grid = make_grid()
    WIN.fill(WHITE)
    running = True
    started = False
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False

        draw_grid()
        pygame.display.update()
        if pygame.mouse.get_pressed()[0]: #Left
            pos = pygame.mouse.get_pos()
            col, row = get_clickedPos(pos)
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


        if pygame.mouse.get_pressed()[2]: #RIGHT
            pos = pygame.mouse.get_pos()
            col, row = get_clickedPos(pos)
            spot = grid[row][col]
            if spot.is_startNode():
                start = None
                spot.resetNode()
            elif spot.is_endNode():
                end = None
                spot.resetNode()
            elif spot.is_barrierNode():
                spot.resetNode()

            spot.drawNode(WIN)
            pygame.display.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not started:
                for rows in grid:
                    for node in rows:
                        node.update_neighbors(grid)

            algorithm(grid, start, end)

            if event.key == pygame.K_c:
                start = None
                end = None
                grid = make_grid()
                draw(grid)
                pygame.display.update()
main()