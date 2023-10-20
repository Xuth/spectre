import math

class Turtle():
    def __init__(self, name = "turtle"):
        self.name = name
        self.x = 0.0
        self.y = 0.0
        self.direction = 0.0

    def __repr__(self):
        return f"[{self.name}: ({self.x}, {self.y}) {self.direction}]"

    def __str__(self):
        return f"({round(self.x,5)}, {round(self.y,5)})"

    def rot(self, degrees):
        self.direction += degrees
        self.direction %= 360.0

    def rotAbs(self, degrees):
        self.direction = degrees % 360.0

    def move(self, dist):
        factor = math.pi / 180.0
        dRad = self.direction * factor

        self.x += math.sin(dRad) * dist
        self.y += math.cos(dRad) * dist


    def moveAbs(self, x, y):
        self.x = x
        self.y = y
        
