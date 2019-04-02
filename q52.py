# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


rectangle = Rectangle(3,4)
print(rectangle.area())

