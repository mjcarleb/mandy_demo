class Rectangle():

    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.width * self.length

    def __str__(self):
        return f"length={self.length} x width={self.width}"

class Square(Rectangle):

    def __init__(self, side):
        self.length = side
        self.width = side


big_thin_rectangle = Rectangle(length=300, width=1)
print(f"The perimeter of a rectangle {big_thin_rectangle.perimeter()}")

square = Square(side=3)
print(f"The perimeter of a square {square.perimeter()}, area = {square.area()}")

print(square)
