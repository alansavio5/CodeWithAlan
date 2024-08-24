# method chaining >>>>>>>>>>> to call multiple methods sequentailly
#                               each call performs an action on same object and returns self

class Car:

    def start(self):
        print("You started the car")
        return self

    def drive(self):
        print("You are driving the car")
        return self

    def brake(self):
        print("You hit the brakes")
        return self

    def stop(self):
        print("You stopped the car")
        return self

car = Car()
car.start()\
    .drive()\
        .brake()\
            .stop()                 # in case when we're using so many functions do like this for readability