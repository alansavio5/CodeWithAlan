# duck typing >>>>>>> concept where the class of an object is less important than the methods
#                       class type is not checked if minimum number of methods/attributes are present
#                           "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")
        
    def talk(self):
        print("This chicken is clucking")

class Person:

    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)

# The Person class expects the object passed to its catch method to have walk and talk methods. 
# It doesn't care if the object is an instance of Duck, Chicken, or any other class, as long as it has these methods.
