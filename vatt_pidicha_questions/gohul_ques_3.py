# wap to find the lcm of a number

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
lcm = num1*num2

for i in range(1,lcm+1):
    if i%num1 == 0 and i%num2 == 0:
        lcm = i
        break
    else:
        continue
print(f"lcm of {num1} and {num2} is {lcm}")