import math
from area.shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.cir_area = 0.0
        self.radius = radius

    def area(self):
        self.cir_area = math.pi * (self.radius ** 2)
        return self.cir_area

    def __str__(self) -> str:
        self.area()
        return 'Circle area can show that ' + str(self.radius) + 'U :' + str(self.cir_area)