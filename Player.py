
from GameObject import GameObject
from ID import ID
import pygame


class Player(GameObject):
    """docstring for Player"""

    def __init__(self, x, y, width, height, id: ID, velX=None):
        super(Player, self).__init__(x, y, width, height, id, velX)
        self.change_posX = 0
        self.centerx = 0
        self.centery = 0

    def tick(self):
        pass

    def render(self, win):
        self.rectangle = pygame.draw.rect(win, self.getColors(),
                         (self.x, self.y, self.width, self.height))
        
        self.centerx = self.rectangle.center[0]
        self.centery = self.rectangle.center[1]