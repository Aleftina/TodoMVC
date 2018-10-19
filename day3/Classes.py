class Shape:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

class Circle(Shape):
    def __init__(self, x, y, r):
        self.r = super().__init__(x, y)


