# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.

import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi


circle = Circle(2)
print(circle.area())


