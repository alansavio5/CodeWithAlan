num = int(input("Enter the number: "))
factorial = 1

if num < 0:
    print("Enter a positive integer")

elif num == 0 or num == 1:
    print(f"The factorial of {num} is 1")

elif num > 0:
    for i in range(1,num+1):
        factorial = factorial*i
    print(f"The factorial of the number {num} is {factorial}")
