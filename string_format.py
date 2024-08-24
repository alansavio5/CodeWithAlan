#{} >>>>>>>>> format fields :- they act as a place holder

animal = "cow"
place = "moon"

print("The {} jumped over the {}".format(animal,place))

print("The {} jumped over the {}".format("lion","africa"))

print("The {1} jumped over the {0}".format(animal,place))

print("The {animal} jumped over the {place}".format(animal="cow",place="moon"))

text = "The {} jumped over the {}"

print(text.format(animal,place))

name = "Alan"

print("Hello, {:10} Nice to meet You".format(name))             #{:10} >>>>>>>>>>>> add 10 padding 

print("Hello, {:<10} Nice to meet You".format(name))            #left allign

print("Hello, {:>10} Nice to meet You".format(name))            #right allign

print("Hello, {:^10} Nice to meet You".format(name))            #center allign

pi = 3.14159

print("Pi is {:.2f}".format(pi))                            #only show 2 decimal points

num1 = 1000000000

print("The number is {:,}".format(num1))                    #add comma(,) after 1000 places

num2 = 16

print("The binary number is {:b}".format(num2))
print("{:}".format(num2))
print("{:x}".format(num2))
print("{:o}".format(num2))