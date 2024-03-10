# Creata a abstract class of shapes and abstract calculate_perimeter method
from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return self.width * self.height
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    

if __name__ == "__main__":
    rectangle = Rectangle(10, 5)
    print(rectangle.calculate_perimeter())
    circle = Circle(5)
    print(circle.calculate_perimeter())