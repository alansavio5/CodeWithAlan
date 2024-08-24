# abstract class >>>>>>>>> a class which contain one or more abstract methods
#                           it prevents the user from creating an object of that class
#                               compels the user to override abstract methods in a child class

# abstract method >>>>>>>>>>> a method which has a declaration but does not have an implementation
from abc import ABC,abstractmethod

class Vehicle(ABC):                 # now, we cannot create an object of this class. Also we need atleast one abstract method of that classmethod
                                    # the children classes should override the abstract method of this class
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You are driving a car")

    def stop(self):
        print("The car is stopped")
        

class Motorcycle(Vehicle):

    def go(self):
        print("You are riding a motorcycle")

    def stop(self):
        print("The motorcycle is stopped")

# vehicle = Vehicle() >>>>>>> we cannot create an object of the abstract class
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()