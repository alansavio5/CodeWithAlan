class Circle:

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius**2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

circle = Circle(5)

print("Area of the circle {}".format(circle.area()))
print("Perimeter of the circle {}".format(circle.perimeter()))
