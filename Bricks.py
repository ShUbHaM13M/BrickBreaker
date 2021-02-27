
import pygame
import random

class Map(object):

    def __init__(self, row, column):

        self.row = row
        self.column = column

        self.m = [[0 for col in range(self.column)] for r in range(self.row)]
        for r in range(self.row):
            for c in range(self.column):
                self.m[r][c] = 1
       
        self.width = 540 / self.column
        self.height = 150 / self.row
        self.lst = []
        
    def render(self, win):
        for r in range(self.row):
            for c in range(self.column):
                if self.m[r][c] == 1:
                    self.x = c * self.width + 45
                    self.y = r * self.height + 50
                    rect = pygame.draw.rect(win, (255, 255, 255), 
                                        (self.x, self.y, self.width, self.height))

        for r in range(self.row):
            for c in range(self.column):
                if self.m[r][c] == 1:
                    self.x = c * self.width + 45
                    self.y = r * self.height + 50
                    rect = pygame.draw.rect(win, (0, 0, 0), 
                                        (self.x, self.y, self.width, self.height), 1)

    def setRenderValue(self, value, row, column):
        self.m[row][column] = value

    def getList(self):
        return self.lst
    
m = Map(2, 3)
