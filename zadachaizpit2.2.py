import math
class Shape:
    def __init__(self, color):
        self.color = color
    def area(self):
        pass
class Rectangle(Shape):
    def __init(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
rectangle = Rectangle(color="Zelen", width=5)
circle = Circle(color="Sin", radius=5)

print(f"Liceto na pravougulnika e {rectangle.area()}")
print(f"Liceto na {circle.color} krug e {circle.area()}")