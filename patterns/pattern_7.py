n = int(input("Enter the number: "))

for i in range(1,n+1):
    count = 1
    for j in range(n,0,-1):
        if j>i:
            print(" ",end=" ")
        else:
            print(count,end=" ")
        count += 1
    print()
