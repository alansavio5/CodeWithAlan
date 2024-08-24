num = int(input("Enter the number: "))
temp = num
sum = 0
l = str(num)

while num > 0:
    digit = num % 10
    sum = sum + (digit**len(l))
    num = num // 10

if sum == temp:
    print("The number is amstrong")

else:
    print("The number is not amstrong")




















