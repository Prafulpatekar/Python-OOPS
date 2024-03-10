import math

class Shape:
    def __init__(self,area) -> None:
        self.area = area

    def compute_area(self):
        self.area = 0


class Cirle(Shape):
    def __init__(self,radius) -> None: 
        self.radius = radius
    
    def compute_area(self):
        self.area = math.pi * self.radius * self.radius

    
if __name__ == "__main__":
    circle = Cirle(5)
    circle.compute_area()
    print(circle.area)