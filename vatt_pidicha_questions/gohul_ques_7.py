# reverse a string without using slicing or methods

string = input("Enter a string: ")
for i in range(len(string),0,-1):
    print(string[i-1],end="")