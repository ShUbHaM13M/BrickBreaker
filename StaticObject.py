
from GameObject import GameObject
import pygame
import ID

class StaticObject(GameObject):

    def __init__(self, x, y, width, height, Id, velX=None):
        super().__init__(x, y, width, height, Id, velX=None)


    def render(self, win):
        pygame.draw.rect(win, self.getColors(), 
                         (self.x, self.y, self.width, self.height))