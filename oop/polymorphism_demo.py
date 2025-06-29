import math


class  Shape:
    def __init__(self):
        pass

    def area(self):
        
        raise NotImplementedError
    

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        #return super().area()()
        return self.length * self.width
      
    def __str__(self):
        return f"The area of the Rectangle is:  {self.area()}"


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi
      
    def __str__(self):
        return f"The area of the Circle is: {self.area()}"
