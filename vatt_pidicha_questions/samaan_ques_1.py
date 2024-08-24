# program to check whether the n th element in a given list

numbers = [10,34,55,1,3,6]
num = int(input())
for i in numbers:
    if i == num:
        print(f"Number found at the index {numbers.index(i)}")
    else:
        print(f"Number not found in list")