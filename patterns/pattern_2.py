n = int(input("Enter a number: "))

for i in range(n):
    for j in range(0,i+1):
        print(i+1,end=" ")
    i+=1
    print()
