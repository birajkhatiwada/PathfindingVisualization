import pygame


RED = (255, 65, 54)
GREEN = (46, 204, 64)
BLUE = (0, 116, 217)
YELLOW = (255, 255, 0)
WHITE = (207, 224, 232)
BLACK = (17, 17, 17)
PURPLE = (133, 20, 75)
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
        self.neighbors = []

    def get_neighbors(self):
        return self.neighbors

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
        if not self.is_endNode():
            self.color = GREEN

    def make_closedNode(self):
        self.color = RED

    def make_barrierNode(self):
        self.color = BLACK

    def resetNode(self):
        self.color = WHITE

    def make_pathNode(self):
        if not self.is_startNode() and not self.is_endNode():
            self.color = PURPLE

    def drawNode(self, win):
        return pygame.draw.rect(win, self.color, (self.x, self.y, GAP, GAP))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row > 0 and not grid[self.row-1][self.col].is_barrierNode():
            self.neighbors.append(grid[self.row-1][self.col])
        if self.row < ROWS-1 and not grid[self.row+1][self.col].is_barrierNode():
            self.neighbors.append(grid[self.row+1][self.col])

        if self.col > 0 and not grid[self.row][self.col-1].is_barrierNode():
            self.neighbors.append(grid[self.row][self.col-1])
        if self.col < ROWS-1 and not grid[self.row][self.col+1].is_barrierNode():
            self.neighbors.append(grid[self.row][self.col+1])



