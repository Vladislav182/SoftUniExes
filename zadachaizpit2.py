import math

3class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass  # Абстрактен метод - ще бъде пренаписан в подкласовете

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Пример на използване на класовете
circle = Circle(color="Зелен", radius=5)
rectangle = Rectangle(color="Син", width=4, height=6)

# Извеждане на площите
print(f"Площ на кръга (цвят: {circle.color}): {circle.area()}")
print(f"Площ на правоъгълника (цвят: {rectangle.color}): {rectangle.area()}")
