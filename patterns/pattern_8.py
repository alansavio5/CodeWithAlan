n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n,n-i-1,-1):
        print(" ",end="")
    for k in range(i,n):
        print("* ",end="")
    print()
