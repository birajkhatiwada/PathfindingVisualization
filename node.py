import pygame


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


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * GAP
        self.y = col * GAP
        self.color = WHITE

    def get_pos(self):
        return self.row, self.col

    def is_startNode(self):
        return self.color == ORANGE

    def is_endNode(self):
        return self.color == BLUE

    def is_openNode(self):
        return self.color == GREEN

    def is_closedNode(self):
        return self.color == RED

    def is_barrierNode(self):
        return self.color == BLACK

    def make_startNode(self):
        self.color = ORANGE

    def make_endNode(self):
        self.color = BLUE

    def make_openNode(self):
        self.color = GREEN

    def make_barrierNode(self):
        self.color = BLACK

    def resetNode(self):
        self.color = WHITE

    def make_pathNode(self):
        self.color = PURPLE

    def drawNode(self, win):
        return pygame.draw.rect(win, self.color, (self.x, self.y, GAP, GAP))

    # def update_neighbors(self, grid):

