def maximum(num1,num2,num3):
    if num1 > num2:
        if num3 > num1:
            max = num3
        elif num1 > num3:
            max = num1
    elif num2 > num1:
        if num2 > num3:
            max = num2
        elif num3 > num2:
            max = num3

    return max

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second nnumber: "))
num3 = int(input("Enter third number: "))

print("The largest among these is: ",maximum(num1,num2,num3))




























