

class Handler(object):
    """docstring for Handler"""

    def __init__(self):
        self.objectList = []

    def tick(self):
        for obj in len(self.objectList):
            obj.tick()

    def render(self, win):
        
        for obj in range(0, len(self.objectList)):
            self.objectList[obj].render(win)

    def add(self, obj) -> None:
        self.objectList.append(obj) 

    def remove(self, obj) -> None:
        try:
            self.objectList.pop(self.objectList.index(obj))
        except ValueError:
            pass
