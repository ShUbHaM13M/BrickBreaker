
class GameObject(object):
    """docstring for GameObject"""

    def __init__(self, x, y, width, height, Id, velX=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Id = Id
        self.velX = velX
        self.dim = (self.x, self.y, self.width, self.height)

    def setColors(self, r, g, b, a=1):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def getColors(self):
        return (self.r, self.g, self.b, self.a)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def tick(self):
        pass

    def render(self, win):
        pass

    def setVel(self, vel):
        self.velX = vel
        
    def getVel(self):
        return self.velX