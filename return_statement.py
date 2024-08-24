#<<<<<<<<<<<< RETURN STATEMENT >>>>>>>>>>>>
#function that return value to the caller
#this value is known as the return value

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def multiply(num1,num2):
    result = num1 * num2
    return result
x = multiply(num1,num2)

print(f"The product of these two numbers is {x}")




