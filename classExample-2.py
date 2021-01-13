# class example with constructtor

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.move()
point.draw()
print(point.x)
print(point.y)

point = Point(y=40, x=20)
point.move()
point.draw()
print(point.x)
print(point.y)
