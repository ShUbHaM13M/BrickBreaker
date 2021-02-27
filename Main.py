
import sys
import pygame
from pygame.locals import *
from ID import ID
from Handler import Handler
from Player import Player
from Ball import Ball
from StaticObject import StaticObject
from Bricks import Map
import time
import math
    
def clamp(val, min, max):
    if val >= max:
        return max
    elif val <= min:
        return min
    else:
        return val

class Main(object):
    """docstring for Main"""

    def __init__(self, width, height, title: str):
        pygame.init()
        pygame.display.set_caption(title)
    
        self.clock = pygame.time.Clock()
        self.WIDTH = width
        self.HEIGHT = height
        self.keys = [False, False]
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.handler = Handler()
        self.score = 0
        self.map = Map(3, 9)

        self.renderScore()
        self.objectRender()

    def renderScore(self):       
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.txt = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.txt_rect = self.txt.get_rect()
        self.txt_rect.center = (640 // 2, 40 // 2)

    def objectRender(self):

        self.player = Player(260, 450, 75, 20, ID.player, 1)
        self.player.setColors(255, 255, 255)
        
        top_goal = StaticObject(10, 40, 620, 1, ID.staticObject)
        top_goal.setColors(255, 255, 255)

        left_border = StaticObject(10, 40, 1, 460, ID.staticObject)
        left_border.setColors(255, 255, 255)

        self.ball = Ball(self.win, self.WIDTH / 2, self.HEIGHT / 2, ID.ball, 10, 5)
        self.ball.setColors(255, 255, 255)

        right_border = StaticObject(630, 40, 1, 460, ID.staticObject)
        right_border.setColors(255, 255, 255)

        self.handler.add(self.ball)
        self.handler.add(self.map)
        self.handler.add(self.player)
        self.handler.add(top_goal)
        self.handler.add(left_border)
        
        self.handler.add(right_border)
        
        self.gameLoop()

    def draw(self):
        self.win.fill((0, 0, 0))
        
        self.win.blit(self.txt, self.txt_rect)
        self.handler.render(self.win)
        pygame.display.flip()
        pygame.display.update()

    def gameLoop(self):

        isRunning = True
        while isRunning:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False
            

            if event.type == pygame.KEYDOWN:
    
                if event.key == K_LEFT:
                    self.keys[0] = True
                elif event.key == K_RIGHT:
                    self.keys[1] = True

            if event.type == pygame.KEYUP:

                if event.key == K_LEFT:
                    self.keys[0] = False
                elif event.key == K_RIGHT:
                    self.keys[1] = False

            if self.keys[0] == True:
                if self.player.x > 10:
                    self.player.x -= 10
            
            elif self.keys[1] == True:
                if self.player.x < self.WIDTH - 90:
                    self.player.x += 10

            else:
                self.player.x = self.player.getX()

            for r in range(self.map.row):
                for c in range(self.map.column):
                    if self.map.m[r][c] > 0:
                        brick_x = int(c * self.map.width + 45)
                        brick_y = int(r * self.map.height + 50)
                        brick_width = int(self.map.width)
                        brick_height = int(self.map.height)
                        rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)

                        if rect.colliderect(self.ball.circle):
                            self.score += 5
                            self.renderScore()
                            self.ball.change_y = -self.ball.change_y
                            self.map.setRenderValue(0, r, c)
                            

            
            self.ball.checkHit(self.player)
            self.ball.bounce(self.WIDTH, self.HEIGHT)

            self.clock.tick(60)

            self.draw()

        pygame.quit()
        sys.exit()


app = Main(640, 500, "BrickBreaker")
