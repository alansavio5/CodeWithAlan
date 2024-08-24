first_name = input("Enter Your first name: ")
last_name = input("Enter Your last name: ")
name = first_name+" "+last_name
age = 22

def hello(name,age):
    print(f"Hello {name}")
    print(f"You are {age} years old")
    print("Have a nice day")
hello(name,age)
