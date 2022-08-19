class Rectangle:
    def __init__(self, length, width) :
        self.length = length
        self.width = width
    def area(self) :
        print("Area of the Rectangle is: ")
        print(self.length * self.width)

r1 = Rectangle(10,5)
r1.area()