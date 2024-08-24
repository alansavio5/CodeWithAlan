# method overriding >>>>>>>> it allows a child class to provide a specific implementation of a method that is already defined in its parent class

class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    def eat(self):
        print("This rabbit is eating")

rabbit = Rabbit()
rabbit.eat()