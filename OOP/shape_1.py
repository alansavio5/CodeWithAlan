import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        self.area=math.pi*(self.radius**2)
        print(f"The area of this circle is {self.area}")

    def perimeter(self):
        self.perimeter=2*math.pi*self.radius
        print(f"The perimeter of this circle is {self.perimeter}")

class Triangle(Shape):

    def __init__(self,side1,side2,side3,breadth,height):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        self.breadth=breadth
        self.height=height

    def area(self):
        self.area=0.5*self.breadth*self.height
        print(f"The area of this triangle is {self.area}")

    def perimeter(self):
        self.perimeter=self.side1+self.side2+self.side3
        print(f"The perimeter of this triangle is {self.perimeter}")

class Rectangle(Shape):
    
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        self.area=self.length*self.breadth
        print(f"The area of this rectangle is {self.area}")

    def perimeter(self):
        self.perimeter=2*(self.length+self.breadth)
        print(f"The perimeter of this rectangle {self.perimeter}")

circle=Circle(5)
triangle=Triangle(5,5,5,5,7)
rectangle=Rectangle(5,5)

circle.area()
circle.perimeter()
triangle.area()
triangle.perimeter()
rectangle.area()
rectangle.perimeter()