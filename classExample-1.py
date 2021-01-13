# class example with out constructor

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point()
point.move()
point.draw()

# assign attribute value

point.x = 10
point.y = 20
print(point.x)
print(point.y)