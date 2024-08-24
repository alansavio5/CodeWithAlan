from car import Car                 # car >>>> module    //      Car >>>> class 

car_1 = Car("BMW","M-5","2018")
car_2 = Car("Chevrolet","Corvette","2020")

print(car_1.manufacturer)
print(car_1.model)
print(car_1.year)

car_2.stop()

print(car_2.manufacturer)
print(car_2.model)
print(car_2.year)

car_1.drive()

print(Car.wheels)
