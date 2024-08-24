number = input("Enter a number: ")
temp = int(number)
sum=0

for i in number:
    sum = sum+int(i)

if temp % sum == 0:
    print("This is a harshad number")
else:
    print("This is not a harshad number")