# class can be a blueprint to create objects 
# first name of class should be in capitals

class Car:      

    wheels = 4                          #class variable >>>>>>>> variables within the class but outside the constructer                   

    def __init__(self,model,year,manufacturer):            # def __init__ to initialize the object, also known as constructor
        self.model = model
        self.year = year                     # model, year, manufacturer, etc. >>>>>>>> attributes
        self.manufacturer = manufacturer
        
    def drive(self):                # methods
        print("This "+self.model+" is driving")

    def stop(self):                 #self >>>>>>>> object on which we currently working on
        print("This "+self.model+" is stopped")
