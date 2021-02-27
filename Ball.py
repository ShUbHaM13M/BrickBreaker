
from GameObject import GameObject
from ID import ID
import pygame

def intersects(rect, r, center):
    """
        1. rectangle and square tangent of the circle overlaps
        2. if circle's center is inside the rectangle
        3. calculate minimum squared distance from the rectangle sides of the circle's center
            if its lower than squared radius then they collide else not
    """
    circle_distance_x = abs(center[0]-rect.centerx)
    circle_distance_y = abs(center[1]-rect.centery)

    if circle_distance_x > rect.width/2.0+r or circle_distance_y > rect.height/2.0+r:
        return False
    
    if circle_distance_x <= rect.width/2.0 or circle_distance_y <= rect.height/2.0:
        return True

    corner_x = circle_distance_x - rect.width/2.0
    corner_y = circle_distance_y - rect.height/2.0
    corner_distance_sq = corner_x ** 2.0 + corner_y ** 2.0
    return corner_distance_sq <= r**2.0

class Ball(GameObject):
    
    def __init__(self, win, center_x, center_y, Id, radius=10, vel=5):
        self.radius = radius
        self.center_x = int(center_x)
        self.center_y = int(center_y)
        self.Id = Id
        self.vel = vel
        self.change_x = -3
        self.change_y = -3
        self.win = win
        self.hit = False
        self.circle = pygame.Rect(self.center_x-self.radius, self.center_y-self.radius
                                , self.radius**2, self.radius**2)


    def getCenter(self):
        return (self.center_x, self.center_y)
    
    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def getX(self):
        pass

    def setX(self):
        pass

    def setY(self):
        pass
    
    def checkHit(self, rect):
        self.hit = rect and intersects(rect, self.radius, self.getCenter())
        if self.hit == True:
            self.change_y *= -self.change_y

    def render(self, win):
        self.circle = pygame.draw.circle(self.win, self.getColors(), 
                        (self.center_x, self.center_y), self.radius, not self.hit)

    
    def getCircle(self):
        return self.circle

    def bounce(self, screen_width, screen_height):

        # if self.change_x <= -3:
        #     self.change_x = -3
        if self.change_y <= -3:
            self.change_y = -3

        self.center_x += self.change_x
        self.center_y += self.change_y
        

        if self.center_x > (screen_width - 10) - self.radius or self.center_x < (self.radius + 10):
            self.change_x *= -1
        if self.center_y < (self.radius + 40):
            self.change_y *= -1
        
        self.render(None)
        