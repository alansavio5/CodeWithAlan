# super() >>>>>>>>>>> used to give access to the methods of a parent class
#                       returns a temperory object of a parent class when used

class Rectangle:

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
class Square(Rectangle):

    def __init__(self,length,breadth):
        super().__init__(length,breadth)

    def area(self):
        return self.length * self.breadth

class Cube(Rectangle):

    def __init__(self,length,breadth,height):
        super().__init__(length,breadth)
        self.height = height
    
    def volume(self):
        return self.length * self.breadth * self.height

square = Square(5,5)
cube = Cube(5,5,5)

print(square.area())
print(cube.volume())